from .models import Profile
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .choices import gender,COUNTRIES
from django.contrib.auth.models import User
from .mailers import Mailgun_send_email,TEXT,HTML,ResetTEXT,ResetHTML
from .auth import makesecret,makeJWT,checkJWT,check_username,make_expiry_JWT,checkExpiryJWT,secretMessage
from .config import EMAIL_ACTIVATION,LOGIN_AFTER_ACTIVATION
from django.contrib.auth import login,authenticate,logout


def signup(request):

    """

        Custom django signup

    """

    data = {'gender': gender}
    errors = {}
    data['countries'] = COUNTRIES
    data['errors']    = errors

    #if user press signup buttom
    if request.method == 'POST':
        #get username ,email ,password and confirm password
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # first_name   = request.POST.get('first_name')
        first_name   = username
        last_name    = request.POST.get('last_name')
        phone        = request.POST.get('phone_number')

        # check username validation
        if not check_username(username):
            #if username is not  valid
            errors['username'] = 'username must contain only letters numbers '
        else:
            # if username is valid
            try :
                #check if username exists or not
                User.objects.get(username=username)
                errors['username'] = 'Username already exists'

            except:
                pass
        #if username is available
        try:
            #If is email is not available
            User.objects.get(email=email)
            errors['email'] = 'Email already exists'
        except:
            pass

        #if username and email are available
        #check length of password
        if len(password) > 8:

            #if password is greater than 8 and has no past errors
            if  password == confirm_password and len(errors) == 0:
                #create user
                get_user = User.objects.create(username=username, email=email)
                #set password
                get_user.set_password(password)
                get_user.save()
                #create token
                token = makesecret()
                #create jwt secret
                secret = makeJWT(get_user.username,token)

                #if Email activation is on
                # ( Can change from account/config.py  EMAIL_ACTIVATION = True/False )
                if EMAIL_ACTIVATION:
                    #Send Email Notification & mark profile inactive
                    profileObj = Profile.objects.create(user=get_user,token=token)
                    Mailgun_send_email(email, 'secret', TEXT(secret), HTML(secret))

                #if email activation is off
                else:
                    #mark profile active
                    profileObj = Profile.objects.create(user=get_user,token=token,active=True)

                #update profile
                profileObj.first_name = first_name
                profileObj.last_name  = last_name
                profileObj.phone      = phone
                profileObj.save()

                return render(request, 'accounts/after_signup_message.html')

            else:
                errors['cpassword'] = 'Passwords Not Matched !'
        else:
            errors['password'] = 'Password Length Must be greater than 8 characters !'

        return render(request, 'accounts/signup.html', data)

    # renders Simple Signup page
    return render(request, 'accounts/signup.html', data)



def activate(request,secret):
    # activate user  Profile
    #check jwt and extract data
    data = checkJWT(secret)
    if data:
        #if data is available
        #get usrname from data
        user = User.objects.get(username=data['username'])
        #get profile object of user
        profileObj = Profile.objects.get(user=user)

        #if key matches to token
        if profileObj.token == data['key']:
            #update profile
            profileObj.active = True
            #create another token
            profileObj.token  = makesecret()
            profileObj.save()

            #login user
            if LOGIN_AFTER_ACTIVATION:
                login(request,user)

            return HttpResponse('Activated')

        return render(request, 'accounts/invalid_signup.html')
    else:
        return render(request, 'accounts/invalid_signup.html')



def loginuser(request,secret_message=''):

    """ Custom user login """

    errors = {}
    #if user enters login credentials
    if request.method == 'POST':
        #username_email if can be email or username
        username_email = request.POST.get('username_email')
        #get password
        password = request.POST.get('password')

        #if user enters email
        if '@' in username_email :

            try:
                #check for email
                user =  User.objects.get(email=username_email)
                #if email password is authenticated
                authenticated = authenticate(username=user.username,password=password)
                if authenticated :
                    #login user
                    login(request,user)
                    #redirect to homepage
                    return redirect('homepage')
                else:
                    errors['password'] = 'Wrong Password !'
            except:
                errors['username_email'] = f"Email address doesn't exists."
        else:

            try:
                #if user enters email
                user =  User.objects.get(username=username_email)
                authenticated = authenticate(username=user.username,password=password)
                #if user is authenticated
                if authenticated :
                    #login user
                    login(request,user)
                    #redirect user
                    return redirect('homepage')
                else:
                    errors['password'] = 'Wrong Password !'
            except:
                errors['username_email'] = f"Username doesn't exists."


        return render(request, 'accounts/login.html', errors)
    else:
        if secret_message:
            errors['message'] = checkJWT(secret_message)
        return render(request, 'accounts/login.html', errors)



def resetpassword(request):
    """ reset password """

    errors = {}
    # if user request for password reset
    if request.method == 'POST':
        #username or email
        username_email = request.POST.get('username_email')

        if '@' in username_email:
            try:
                #check for valid email
                user =  User.objects.get(email=username_email)
            except:
                user = None
                errors['username_email'] = f"Email address doesn't exists."
        else:
            try:
                # check for valid username
                user =  User.objects.get(username=username_email)
            except:
                user = None
                errors['username_email'] = f"Username doesn't exists."

        if user:
            #if email or username exists
            #create token
            token = makesecret()
            #update profile token
            Profile.objects.filter(user=user).update(token=token)
            #create expiry Jwt token with profile token
            secret = make_expiry_JWT(user.username,token)
            # Send reset email to user's email
            Mailgun_send_email(user.email, 'Reset Password', ResetTEXT(secret), ResetHTML(secret))
            message = 'Please check your email to reset your password !'
            return redirect('login_with_message', secret_message=secretMessage(message))

    return render(request, 'accounts/resetpassword.html', errors)


def reset_password(request,secret):
    """
        Checks reset url if correct then update password

    """
    #check jwt
    data = checkExpiryJWT(secret)
    content = dict()
    status  = False
    message = ''
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        #if jwt is not expired
        if data:
            #get user objects
            user = User.objects.get(username=data['username'])
            profileObj = Profile.objects.get(user=user)
            #if key matched
            if profileObj.token == data['key']:
                status = True
                #if password is greater than 8
                if len(password) > 8:
                    # if password matched
                    if password == confirm_password :
                        # set password
                        user.set_password(password)
                        user.save()
                        #create new token
                        profileObj.token = makesecret()
                        profileObj.save()
                        message = 'Password Changed Successfully'
                        return redirect('login_with_message',secret_message=secretMessage(message))
                    else:
                        message = 'Passwords Not Matched !'
                else:
                    message = 'Password Length Must be greater than 8 characters !'

            else:
                message = "Link Expired"

        else:
            message = 'Link Expired'

    else:
        #if jwt is not expired
        if data:
            #get user object
            user = User.objects.get(username=data['username'])
            #get profile object
            profileObj = Profile.objects.get(user=user)

            #if token == key
            if profileObj.token == data['key']:
                status = True
            else:
                message = "Link Expired"
        # if jwt is expired or key mismatched
        else:
            message = 'Link Expired'
    content['message'] = message
    content['status'] = status
    return render(request, 'accounts/reset_change_pwd.html', content)


def logoutuser(request):
    """ logout user """
    logout(request)
    return redirect('login')

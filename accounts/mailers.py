import smtplib
# from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

#
# def Twilio(body,mobile):
#     client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)
#     message = client.messages.create(
#         from_= config.FROM_NO,
#         to=config.COUNTRY_CODE+str(mobile),
#         body= body
#     )

def Mailgun_send_email(to,subject,text,html):

    from_email = 'Business Signup'
    msg = EmailMultiAlternatives(subject, text, from_email, [to])
    msg.attach_alternative(html, "text/html")
    msg.send()

    # return requests.post(
    #     "https://api.mailgun.net/v3/"+config.MAIL_GUN_DOMAIN+"/messages",   # domain url + /messages
    #     auth=("api", config.MAIL_GUN_API),                                  # api key in domain settings
    #     data={"from": "Diverse Aquaria <"+config.MAIL_GUN_FROM+">",            # mailgun @ domain.com (sandbox)
    #                   "to": to,                                             # add more email use list
    #           "subject": subject,
    #           "text": text,
    #           "html": html})


def TEXT(secret):
    return f'http://127.0.0.1:8000/accounts/activate/{secret}'

def HTML(secret):
    return f'<h5><a href="http://127.0.0.1:8000/accounts/activate/{secret}">Click here to activate account</a></h5>'

def ResetTEXT(secret):
    return f'http://127.0.0.1:8000/accounts/reset_password/{secret}'

def ResetHTML(secret):
    return f'<h5><a href="http://127.0.0.1:8000/accounts/reset_password/{secret}">Click here to reset yourpassword</a></h5>'

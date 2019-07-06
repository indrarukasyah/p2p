from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    # path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('login/<secret_message>',views.loginuser,name='login_with_message'),
    path('reset/',views.resetpassword,name='resetpassword'),
    path('reset_password/<secret>',views.reset_password,name='reset'),
    path('activate/<secret>',views.activate,name='activate'),
]

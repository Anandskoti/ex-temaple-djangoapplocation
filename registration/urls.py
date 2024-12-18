"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from app1 import views
from django.contrib.auth import views as auth_views #type:ignore
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('reviewer_signup/',views.Reviewer_SignupPage,name='reviewer_signup'),
    path('controller_signup/',views.Controller_SignupPage,name='controller_signup'),
    path('approver_signup/',views.Approver_SignupPage,name='approver_signup'),
    path('admin_signup/',views.Admin_SignupPage,name='admin_signup'),
    


    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('reviewer_login/',views.Reviewer_LoginPage,name='reviewer_login'),
    path('controller_login/',views.Controller_LoginPage,name='controller_login'),
    path('approver_login/',views.Approver_LoginPage,name='approver_login'),
    path('admin_login/',views.Admin_LoginPage,name='admin_login'),
   

    path('thirdpage/',views.Third_Page,name='thirdpage'),

    path('authorizer/',views.authorizer,name='authorizer'),
        path('fifthpage/',views.fifthpage,name='fifthpage'),



    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
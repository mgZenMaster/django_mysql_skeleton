from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from forms import LoginForm


def welcome(request):
    return render(request, 'layout.jinja2')


class LoginView(LoginView):

    template_name = "login.jinja2"
    authentication_form = LoginForm


class LogoutView(LogoutView):

    template_name = "logout.jinja2"

    pass


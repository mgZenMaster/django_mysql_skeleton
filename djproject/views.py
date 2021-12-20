from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.decorators import method_decorator
from django_jinja.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from .forms import LoginForm, UserForm


def welcome(request):
    return render(request, 'layout.jinja2')


class LoginView(LoginView):

    template_name = "login.jinja2"
    authentication_form = LoginForm


class LogoutView(LogoutView):

    template_name = "logout.jinja2"

    pass


@method_decorator([login_required(login_url='/admin/login/'), ], name='dispatch')
class CreateUserView(CreateView):

    form_class = UserForm
    model = User
    template_name = 'user/edit.jinja2'

    def get_success_url(self):
        return reverse('list-users')


@method_decorator([login_required(login_url='/admin/login/'), ], name='dispatch')
class EditUserView(UpdateView):

    form_class = UserForm
    model = User
    template_name = 'user/edit.jinja2'

    def get_success_url(self):
        return reverse('list-users')


@method_decorator([login_required(login_url='/admin/login/'), ], name='dispatch')
class ListUserView(ListView):

    model = User
    template_name = 'user/list.jinja2'

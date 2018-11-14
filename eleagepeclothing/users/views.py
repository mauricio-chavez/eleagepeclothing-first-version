from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy

from django.views.generic import FormView

from users.forms import SignupForm


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass

def user_detail(request):

	return render(request, 'shop/details.html', context)

class SignupView(FormView):

	template_name = 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class LoginView(auth_views.LoginView):

	template_name = 'users/login.html'
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    # def get(self, request):
    #     return HttpResponse("Capstone Project Home")


class Login(View):
    def post(self, request):
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"/profile/{user.pk}")
        
        else:
            return HttpResponse("Unable to login!", content_type="text/plain")


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(
                user=request.user, 
                name="New User", 
                )
            return redirect(f"/profile/{user.pk}")
        else:
            return HttpResponse("Unable to create profile!", content_type="text/plain")




        

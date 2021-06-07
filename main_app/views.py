from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Trail, CommunityHike

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class Login(View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"home")
        
        else:
            return HttpResponse("Unable to login!", content_type="text/plain")

    def get(self,request):
        return render(request, "login.html")


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = request.POST.get("email")
            user.save()
            login(request, user)
            Profile.objects.create(
                user=request.user, 
                first_name = request.POST.get("first_name"),
                last_name = request.POST.get("last_name"),
                email = request.POST.get("email"),
                )
            return redirect(f"customlogin")
        else:
            print(request.POST, form.errors)
            return HttpResponse("Unable to create profile, please try again.", content_type="text/plain")

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)


class ShowProfile(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {"user": user, "first_name": Profile.objects.filter(first_name=user.profile.first_name)}
        return render(request, "profile.html", context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Profile, self).for_valid(form)

    
class UpdateProfile(View):
    def post(self, request, pk):
        profile = Profile.objects.get(user=pk)
        profile.first_name = request.POST["first_name"]
        profile.last_name = request.POST["last_name"]
        profile.email = request.POST["email"]
        profile.save()
        return redirect(f"/profile/{pk}")

        # if form.data['first_name', 'last_name', 'email'] is None:
        #     return 



class TrailCategory(TemplateView):
    template_name = "trails_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trails"] = Trail.objects.filter(category__icontains=self.kwargs["category"])
        print(context)
        return context



class FavTrails(TemplateView):
    template_name = "user_favorite_trails.html"




class CreateCommunityEvent(CreateView):
    model = CommunityHike
    fields = ['date', 'description', 'time']
    template_name = "create_event.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user.profile
        form.instance.trail = Trail.objects.get(pk=self.kwargs["trail_pk"])
        return super(CreateCommunityEvent, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trail"] = Trail.objects.get(pk=self.kwargs["trail_pk"])
        print(context)
        return context
    
    def get_success_url(self):
        return reverse('viewevent', kwargs={'pk': self.object.pk})



class ViewCommunityEvent(DetailView):
    model = CommunityHike
    template_name = "view_event.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["communityhike"] = CommunityHike.objects.all()
        print(context)
        return context



class DeleteCommunityEvent(DeleteView):
    model = CommunityHike
    template_name = "event_delete_confirmation.html"
    success_url = "/"



class Info(TemplateView):
    template_name = "info.html"



            




        

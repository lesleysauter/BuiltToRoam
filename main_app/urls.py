from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/<int:pk>/', views.ShowProfile.as_view(), name="profile"),
    path('login/', views.Login.as_view(), name="customlogin"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('favtrails/<int:pk>/', views.FavTrails.as_view(), name="favtrails"), 
    path('trailcategory/', views.TrailCategory.as_view(), name="trailcategory"),
    path('info/', views.Info.as_view(), name="infopage"),
    path('createcommunityevent/', views.CreateCommunityEvent.as_view(), name="createevent"),
    path('viewcommunityevent/', views.CreateCommunityEvent.as_view(), name="viewevent"),


]
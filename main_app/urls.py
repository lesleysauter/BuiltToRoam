from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/<int:pk>/', views.ShowProfile.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.UpdateProfile.as_view(), name="updateProfile"),
    path('login/', views.Login.as_view(), name="customlogin"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('favtrails/', views.FavTrails.as_view(), name="favtrails"), 
    path('trailcategory/<str:category>/', views.TrailCategory.as_view(), name="trailcategory"),
    path('info/', views.Info.as_view(), name="infopage"),
    path('createcommunityevent/', views.CreateCommunityEvent.as_view(), name="createevent"),
    path('viewcommunityevent/', views.ViewCommunityEvent.as_view(), name="viewevent"),


]
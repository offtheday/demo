from django.urls import path
from django.conf.urls import url
from userSystem import views
from django.views.generic import RedirectView


urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView,name='register'),
    path('AdminHomePage/<str:username>/<str:password>/', views.AdminHomePageView,name="AdminHomePage"),
    path('HomePage/<str:username>/<str:password>/', views.HomePageView,name="HomePage"),
    path('documentManagement/<str:username>/<str:password>/', views.DocumentManagementView,name="documentManagement"),
    #path('library/<str:username>/<str:password>/', views.LibraryView,name="library"),
    ]
    #<str:username>/<str:password>/
    
    
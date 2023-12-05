from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profil/", views.profil, name="profil"),
    path("header/", views.header, name="header"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("register", views.register, name="register"),
    path('admin/', admin.site.urls),
#    path('web_project/', include('web_project.urls')), 
   
    
]


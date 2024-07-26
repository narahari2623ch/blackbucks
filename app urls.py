from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('register/', views.register, name='register'),
        path('login/', views.Login, name='login'),
        path('logout/', views.Logout, name='logout'),
        path('', views.index, name ='index'),
]

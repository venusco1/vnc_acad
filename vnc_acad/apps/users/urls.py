from django.urls import path,include
from apps.users import views

apps_name = "users"
   
urlpatterns = [
    path('', views.users, name='users'),
]

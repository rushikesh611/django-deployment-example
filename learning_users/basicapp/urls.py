from django.urls import path,include
from . import views

#template url

app_name = 'basicapp'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]

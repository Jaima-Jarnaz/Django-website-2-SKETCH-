from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("user",views.user,name='user'),
    #path('upload',views.upload_image,name='upload_image'),
]
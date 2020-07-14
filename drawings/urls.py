from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('samima',views.samima,name='samima'),
    path('tonima',views.tonima,name='tonima'),
    path('mithila',views.mithila,name='mithila'),  
    path('isrita',views.isrita,name='isrita'),
    path('bintu',views.bintu,name='bintu'),
    path('puspo',views.puspo,name='puspo'),
]
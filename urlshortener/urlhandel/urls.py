from django.urls import path
from . import views

urlpatterns=[
    path('', views.make,name="make"),
    path('<str:token>', views.home ,name="home")
]
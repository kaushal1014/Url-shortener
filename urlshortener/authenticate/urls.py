from django.urls import path
from . import views
app_name='authenticate'
urlpatterns=[
    path('', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path("urlshortner/", views.urlshortner, name='urlshortner')
]
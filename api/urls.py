from django.urls import path
from . import views
urlpatterns = [
    path('generate-password', views.generate_password),
    path('random-number', views.random_number),
    path('weather', views.weather),
]

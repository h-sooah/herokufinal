from django.urls import path, include
from . import views

urlpatterns = [
    path('social/', views.social, name="social"),
    path('social/', include("allauth.urls")),
]
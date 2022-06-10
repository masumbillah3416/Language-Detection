from django.urls import path
from . import views

urlpatterns = [
    path('check-language/', views.single_check),
]
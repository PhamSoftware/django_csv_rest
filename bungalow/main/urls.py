from django.urls import path

from main import views

urlpatterns = [path("homes/", views.home_list), path("homes/<int:pk>/", views.home_detail)]

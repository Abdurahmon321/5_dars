from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all_homes', views.all_homes, name="all_homes"),
    path("home_detail/<int:id>", views.home_detail, name="home_detail"),
]

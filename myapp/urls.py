from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name = "Home"),
    path("registerr",views.registration,name="registerr"),
    path("view/", views.vieww, name = "view")
]
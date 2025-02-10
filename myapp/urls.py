from django.urls import path
from . import views

urlpatterns=[
    path("home", views.home, name = "Home"),
    path("registerr",views.registration,name="registerr"),
    path("", views.vieww, name = "view"),
    path("detailview/<str:pk>",views.detailvieww,name="detailview"),
    path('userlog/',views.userlog,name="userlogs"),
    path('logins/',views.loginn,name='logins'),
    path('userreg/',views.reg2,name='userreg')
]
from django.urls import path
from . import views

urlpatterns=[
    path("home", views.home, name = "Home"),
    path("registerr",views.registration,name="registerr"),
    path("", views.vieww, name = "view"),
    path("detailview/<str:pk>",views.detailvieww,name="detailview"),
    path('userlog/',views.userlog,name="userlogs"),
    path('logins/',views.loginn,name='logins'),
    path('userreg/',views.reg2,name='userreg'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/increment/<int:cart_item_id>/', views.increment_quantity, name='increment_quantity'),
    path('cart/decrement/<int:cart_item_id>/', views.decrement_quantity, name='decrement_quantity')  

]
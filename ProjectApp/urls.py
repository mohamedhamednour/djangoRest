from django.urls import path,include
from ProjectApp import views
urlpatterns = [
    path('product/', views.productss.as_view() , name='product'),
    path('orderby_price', views.orderby_price, name='orderby_price'),
    path('Order_item', views.Order_item.as_view(), name='Order_item'),
    path('cart_item', views.cart_item.as_view(), name='cart_item'),
    path('category/<str:categ_name>', views.categoryname, name='categ_name'),
    path('getusercart/<int:id>', views.getusercart, name='getusercart'),
    path('getuserorder/<int:id>', views.getuserorder, name='getuserorder'),
    path('allproduct', views.allproduct, name='allproduct'),

]
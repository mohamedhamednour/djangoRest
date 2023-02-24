from rest_framework import generics
from rest_framework.response import Response
from .models import Product, OrderItem, Cart
from .api import Products, order, cart
from rest_framework.decorators import api_view
from rest_framework.permissions import DjangoModelPermissions
from http import HTTPStatus


# products generics post and  get


class productss(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = Products
    permission_classes = [DjangoModelPermissions]



# order
class Order_item(generics.ListCreateAPIView):

    queryset = OrderItem.objects.all()
    serializer_class = order
# cart


class cart_item(generics.ListCreateAPIView):

    queryset = Cart.objects.all()
    serializer_class = cart
# register






# order_by by price
@api_view(['GET'])
def orderby_price(request):
    queryset = Product.objects.all().order_by('-price')
    data = Products(queryset, many=True).data
    return Response(data)


# serch by name
@api_view(['GET'])
def categoryname(request, categ_name):
    queryset = Product.objects.filter(name=categ_name)
    data = Products(queryset, many=True).data
    return Response(data)




# get user cart
@api_view(['GET'])
def getusercart(request, id):
    queryset = Cart.objects.filter(order_user=id)
    data = cart(queryset, many=True).data
    return Response(data)


# get user order
@api_view(['GET'])
def getuserorder(request, id):
    queryset = OrderItem.objects.filter(order_user=id)
    data = order(queryset, many=True).data
    return Response(data)


# all Product
@api_view(['GET'])
def allproduct(request):
    queryset = Product.objects.all()
    data = Products(queryset, many=True).data
    return Response(data)
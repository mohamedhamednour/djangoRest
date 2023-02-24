from django.test import TestCase
from django.urls import reverse, resolve
from ProjectApp import views


class UrlTest(TestCase):

    def test_url_product(self):
       path = reverse('product')
       self.assertTrue(resolve(path).func, views.productss)

    def test_url_orderby_price(self):
       path = reverse('orderby_price')
       self.assertTrue(resolve(path).func, views.orderby_price)

    def test_url_Order_item(self):
        path = reverse('Order_item')
        self.assertTrue(resolve(path).func, views.Order_item)

    def test_url_cart_item(self):
        path = reverse('cart_item')
        self.assertTrue(resolve(path).func, views.cart_item)

    def test_url_allproduct(self):
        path = reverse('allproduct')
        self.assertTrue(resolve(path).func, views.allproduct)


from django.contrib.auth.models import User
from django.test import TestCase , Client
from django.urls import reverse

from ProjectApp.models import Product, Cart


class ViewTest(TestCase):

    def setUp(self):

        self.client = Client()

    def test_product_post(self):
        user = User.objects.create_user(username='hamednour', password='password')
        prodcts = Product.objects.create_user(admin=user, name='password' , price=200.0)


        self.client.post(reverse('cart_item'),{
            "order_user":user , 'product':prodcts , 'quantity':1,'total':300
        })
        card = Cart.objects.get(id=1)
        self.assertEqual(card.quantity, 1)


    def test_all_product(self):
        response = self.client.get(reverse('allproduct'))
        self.assertEqual(response.status_code, 200)

    def test_serch_name(self):

        response = self.client.get(reverse('orderby_price'))
        self.assertEqual(response.status_code, 200)

    def test_product(self):
        response = self.client.get(reverse('product'))
        self.assertEqual(response.status_code, 200)

    def test_orderby_price(self):
        response = self.client.get(reverse('orderby_price'))
        self.assertEqual(response.status_code, 200)

    def test_order_item(self):
        response = self.client.get(reverse('Order_item'))
        self.assertEqual(response.status_code, 200)



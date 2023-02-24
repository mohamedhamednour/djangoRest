from django.test import TestCase
from ProjectApp.models import Product
from django.contrib.auth.models import User



class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(id=2, username='hamednour', password='password')

        Product.objects.create(admin=user, name='polo', price=300.0)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_product_detils(self):
        author = Product.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEqual(str(author), expected_object_name)






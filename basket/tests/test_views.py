from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name='django', slug='django')
        self.user1 = User.objects.create_user(username='user1', password='test12345')
        self.prod1 = Product.objects.create(category_id=1, title='testproduct',
                                            created_by_id=1, slug='test', price=20.2, in_stock=True,
                                            is_active=True, image='django.jpg')
        self.prod2 = Product.objects.create(category_id=1, title='testproduct2',
                                            created_by_id=1, slug='test2', price=30.3, in_stock=True,
                                            is_active=True, image='django.jpg')
        self.prod3 = Product.objects.create(category_id=1, title='testproduct3',
                                            created_by_id=1, slug='test3', price=30.1, in_stock=True,
                                            is_active=True, image='django.jpg')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 3, "action": "post"}, xhr=True)
        
    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code,200)

    def test_basket_add(self):
        """
        Test adding to the basket 
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':6})

        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(),{'qty':4})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(reverse('basket:basket_delete'), {"productid": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':3,'subtotal':'90.90'})
    
    def test_basket_update(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(reverse('basket:basket_update'), {"productid": 2,  "productqty": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':3,'subtotal':'80.80','itemtotal':'60.60'})
        print(response.json())
from importlib import import_module

from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings

from store.views import *
from store.models import Category, Product

# @skip('deponstarting skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.cat1 = Category.objects.create(name='django', slug='django')
        self.user1 = User.objects.create_user(username='user1', password='test12345')
        self.prod1 = Product.objects.create(category_id=1, title='testproduct',
                                            created_by_id=1, slug='test', price=2.2, in_stock=True,
                                            is_active=True, image='django.jpg')

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_product_deatil_url(self):
        response = self.c.get(reverse('store:product_detail', kwargs={'slug': 'test'}))
        self.assertEqual(response.status_code, 200)

    def test_category_deatil_url(self):
        response = self.c.get(reverse('store:category_list', kwargs={'category_slug': 'django'}))
        self.assertEqual(response.status_code, 200)

    def test_home_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # def test_view_function(self):
    #     request = self.factory.get('/')
    #     response = all_products(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>Home</title>',html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code,200)

    def test_url_alowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='example.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='127.0.0.0.1')
        self.assertEqual(response.status_code, 200)

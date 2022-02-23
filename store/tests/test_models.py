from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry2(self):
        """
        Test Category model Defaul name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create_user(username='user1', password='test12345')
        self.data1 = Product.objects.create(category_id=1, title='testproduct', created_by_id=1,
                                            slug='test', price=2.2, in_stock=True, is_active=True, image='django.jpg')

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "testproduct")

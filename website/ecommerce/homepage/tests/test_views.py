from django.test import TestCase, Client
from django.urls import reverse
from website.ecommerce.homepage.models import Customer, Product, Order, OrderItem


class TestViews(TestCase):

    def test_store_GET(self):
        client = Client()

        response = client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')




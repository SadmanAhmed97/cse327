import unittest
from django.urls import reverse, resolve
from .views import store, cart, checkout, updateItem


class TestUrls(unittest.TestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        print(resolve(url))
        self.assertEqual(resolve(url).func, store)

        url = reverse('cart')
        print(resolve(url))
        self.assertEqual(resolve(url).func, cart)

        url = reverse('checkout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, checkout)

        url = reverse('update_item')
        print(resolve(url))
        self.assertEqual(resolve(url).func, updateItem)

from django.test import TestCase

from .models import ShoppingCart


class ShoppingCartModelTests(TestCase):

    def test_sum_prices(self):

        cart = ShoppingCart(prices_sum=70)
        cart.save()
        self.assertEqual(cart.prices_sum, 70)
        cart.sum_prices()
        self.assertEqual(cart.prices_sum, 0)
from django.test import TestCase

# Create your tests here.
class FooBarTestCase(TestCase):
    def setUp(sefl):
        self.x = 0
    def test_foo(self):
        """Test foo"""
        self.assertEqual(self.x, 0)
    def test_bar(self):
        """Test bar"""
        self.assertEqual(self.x, 1)

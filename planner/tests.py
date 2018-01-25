from django.test import TestCase
from planner.models import Yarn

# Create your tests here.
class YarnTestCase(TestCase):
    def setUp(self):
        pass
    def test_TEX(self):
        """Test TEX"""
        yarn = Yarn(numbering_system='TEX', number='2/2')
        self.assertEqual(yarn.tex_number, 4)

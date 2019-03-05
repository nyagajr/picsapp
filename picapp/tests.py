from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.park= Category(category_name = 'National park')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.park,Category))

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.locale= Category(loc_name = 'Madagascar')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.locale,Location))

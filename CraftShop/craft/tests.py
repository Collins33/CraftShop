from django.test import TestCase
from .models import Artist,categories,Craft
# Create your tests here.
#test the Artist model
class ArtistTestClass(TestCase):
    #this method will be run before each test
    def setUp(self):
        self.artist=Artist(first_name="collins",last_name="njau",email="collinsnjau39@gmail.com")


    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.artist,Artist))

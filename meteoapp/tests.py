
from unicodedata import name
from django.test import TestCase
from meteoapp.models import City # en fonction de l'endroit ou l'on lance le test, l'import change

class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(name="lille")
        

    def test_for_test_City_name_length(self):
     
        lille = City.objects.get(name="lille")
        self.assertEqual(lille.test_for_test_City_name_length(),100)

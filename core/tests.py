from django.test import TestCase
# core models
from .models import CarModel
# seo models
from seo.models import SeoModel

class TestCarModel(TestCase):
    def test_create_model(self):
        # crear instancia de CarModel
        model = CarModel.objects.create(
            # direct fields
            name = 'Crv',
            slug = 'c-r-v',
            description = 'Cross Over Very Good Vehicle',

            
            # inherited fields
            seo_title = 'The best Car in its category',
            seo_description = 'this car has been around for decades, the crv is mostly know by been a reliable car',
        )
        
        # assert direct fields works
        self.assertEqual(model.name,'Crv')
        self.assertEqual(model.slug,'c-r-v')
        self.assertEqual(model.description,'Cross Over Very Good Vehicle')

        # assert inherited fields works

        self.assertEqual(model.seo_title,'The best Car in its category')
        self.assertEqual(model.seo_description,'this car has been around for decades, the crv is mostly know by been a reliable car')


        # assert that this class has a parent with this name
        self.assertEqual(issubclass(CarModel,SeoModel),True)
    


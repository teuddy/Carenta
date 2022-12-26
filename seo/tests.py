from django.test import TestCase
from .models import SeoModelTranslation, Translation


class TestTranslationModel(TestCase):
    def test_get_translated_object_id(self):
        # creamos un modelo que extienda de *Translation*
        class MyTestSeoModelTranslation(Translation):
                #fields
                def get_translated_object_id(self):
                        return 'some',1
                def get_translated_keys(self):  
                    return {}

        obj = MyTestSeoModelTranslation()
        self.assertEqual(obj.get_translated_object_id(),('some',1))
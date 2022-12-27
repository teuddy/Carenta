from django.test import TestCase
# core models
from .models import Make, Model
from django.utils.text import slugify

import secrets

# class TestCarModel(TestCase):
#     # crear instancia de CarModel
#     def setUp(self):
#         self.model = CarModel.objects.create(
#             # direct fields
#             name = 'Crv',
#             slug = 'c-r-v',
#         )
#         self.model_translation_english = CarModelTranslation.objects.create(
#             model = self.model,
#             description = "This is some nice description of the crv that going the to ctv page",
#             seo_title = 'Engglish Title For The Crv, *this going for the title page*',
#             seo_description = "English Title For Crv *this is going for the description page"
#         )
#         self.model_translation_spanish = CarModelTranslation.objects.create(
#             model = self.model,
#             description = "esto es una descripcon en español que va para algun sitio de la apgina de la crv ",
#             seo_title = 'Titulo en Espanol para la crv, *esto va a aparecer en titulo*',
#             seo_description = "Descripcion en español para la crv *esto va para la descriotion de la pagina*"
#         )
#         self.model_translation_france = CarModelTranslation.objects.create(
#             model = self.model,
#             description = "le france descripcione para la crv",
#             seo_title = 'titule en france pa la crv *',
#             seo_description = "descripcione en france para la crv*"
#         )
#     def test_create_model(self):
#         # assert direct fields works
#         self.assertEqual(self.model.name,'Crv')
#         self.assertEqual(self.model.slug,'c-r-v')

#     def test_create_a_model_translation(self):
#          # test modeltranslation fields
#         field_names = [field.name for field in self.model_translation_english._meta.get_fields()]
#         self.assertEqual(field_names, ['id','language_code','seo_title', 'seo_description', 'model', 'description',])
#         # test that the model crv has two translations 
#         self.assertEqual(self.model.translation.count(),3)

#     def test_translation_method(self):
#         pass
    


def generate_random_slug(string):
    # generate a random token
    token = secrets.token_hex(8)
    # create a slug by slugifying the string and appending the token
    slug = f"{slugify(string)}-{token}"
    return slug


class TestCarModel(TestCase):
    def setUp(self):
        # creates 5 'Make' table rows  
        make_names = ['Honda', 'Toyota', 'Ford', 'Chevrolet', 'Nissan']
        for name in make_names:
            self.name = Make.objects.create(name=name,slug=generate_random_slug(name))

        # create 5 models for each make
        models_by_make = {
            'Honda': ['Accord', 'Civic', 'Fit', 'CR-V', 'Odyssey'],
            'Toyota': ['Camry', 'Corolla', 'Prius', 'RAV4', 'Highlander'],
            'Ford': ['Fiesta', 'Focus', 'Mustang', 'Explorer', 'Escape'],
            'Nissan': ['Sentra', 'Maxima', 'Versa', 'Altima', 'Murano'],
            'Chevrolet': ['Blazer', 'Equinox', 'Captiva', 'Tracker', 'Traverse']
        }

    # create the models for each make
        for make_name, model_names in models_by_make.items():
            # get the make instance from the database
            make = Make.objects.get(name=make_name)
            # create the models for the current make
            for model_name in model_names:
                Model.objects.create(name=model_name, make=make,slug=generate_random_slug(model_name))

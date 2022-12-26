from django.db import models
from seo.models import SeoModel
from seo.models import SeoModelTranslation


#utils 
from django.db.models import TextField


class CarModel(SeoModel):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=255,
        unique=True,
        allow_unicode=True
    )
    description = TextField(blank=True)




class CarModelTranslation(SeoModelTranslation):
    model = models.ForeignKey(
        CarModel,
        related_name = 'translation',
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    def get_translated_object_id(self):
        return "Model", self.model_id

    def get_translated_keys(self):
        translated_keys = super().get_translated_keys()
        translated_keys.update(
            {
                "name": self.name,
                "description": self.description,
            }
        )
        return translated_keys

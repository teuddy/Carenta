# core packages
from django.db import models
# validations core packages
from django.core.validators import MaxLengthValidator
# utils 
from typing import Any, Dict, Tuple, Union



# ABSTRACT CLASS 
class SeoModel(models.Model):
    seo_title = models.CharField(
        max_length = 70,
        blank = True,
        null = True,
        validators = [
            MaxLengthValidator(70)
        ] 
    )
    seo_description = models.CharField(
        max_length = 300,
        blank = True,
        null = True,
        validators =[
            MaxLengthValidator(300)
        ]
    )
    class Meta:
        abstract = True

# ABSTRACT CLASS
class Translation(models.Model):
    language_code = models.CharField(
        max_length = 35 
    )
    class Meta:
        abstract = True

    def get_translated_object_id(self) -> Tuple[str, Union[int, str]]:
        raise NotImplementedError(
            "Models extending Translation should implement get_translated_object_id"
        )

    def get_translated_keys(self) -> Dict[str, Any]:
        raise NotImplementedError(
            "Models extending Translation should implement get_translated_keys"
        )

    def get_translation_context(self) -> Dict[str, Any]:
        return {}

# ABSTRACT CLASS 
class SeoModelTranslation(Translation):
    seo_title = models.CharField(
        max_length=70, blank=True, null=True, validators=[MaxLengthValidator(70)]
    )
    seo_description = models.CharField(
        max_length=300, blank=True, null=True, validators=[MaxLengthValidator(300)]
    )

    class Meta:
        abstract = True

    def get_translated_keys(self):
        return {
            "seo_title": self.seo_title,
            "seo_description": self.seo_description,
        }
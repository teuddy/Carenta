from django.db import models
# from seo.models import SeoModel
# from seo.models import SeoModelTranslation


class Make(models.Model):
    name = models.CharField(max_length=70) 
    slug = models.SlugField(max_length=255,
        unique=True,
        allow_unicode=True
    )
 

# CAR > MODEL, GENERATION, SERIE, TRIM 
class Car(models.Model):
    year = models.SmallIntegerField()
    mileage = models.SmallIntegerField()
    vin = models.CharField(max_length=70) 
    availability  = models.BooleanField(default=False)
    model = models.ForeignKey("Model",on_delete = models.CASCADE)
    generation = models.ForeignKey('Generation',on_delete = models.CASCADE)
    serie = models.ForeignKey('Serie',on_delete=models.CASCADE)
    trim = models.ForeignKey('Trim',on_delete=models.CASCADE)


# MODEL > MAKE 
class Model(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=255,
        unique=True,
        allow_unicode=True
    )
    make = models.ForeignKey(
        "Make",
        on_delete= models.CASCADE,
        related_name = 'models' 
    )


# GENERATION > MODEL 
class Generation(models.Model):
    name = models.CharField(max_length=200)
    year_begin = models.SmallIntegerField()
    year_end = models.SmallIntegerField()
    model = models.ForeignKey(
        'Model',
        on_delete= models.CASCADE,
        related_name = 'generations'
    ) 

# SERIE > MODEL, GENERATION 
class Serie(models.Model):
    name = models.CharField(max_length=200)
    model = models.ForeignKey(
        'Model',
        on_delete = models.CASCADE
    )
    generation  = models.ForeignKey(
        'Generation',
        on_delete = models.CASCADE
    )

# TRIM > MODEL, SERIE
class Trim(models.Model):
    name = models.CharField(max_length=70) 
    start_production = models.SmallIntegerField()
    end_production = models.SmallIntegerField()
    model  = models.ForeignKey(
        'Model',
        on_delete = models.CASCADE
    )
    serie  = models.ForeignKey(
        'Serie',
        on_delete = models.CASCADE
    )

# EQUIPMENT > TRIM 
class Equipment(models.Model):
    name = models.CharField(max_length=70) 
    year = models.SmallIntegerField()
    trim = models.ForeignKey(
        'Trim',
        on_delete= models.CASCADE,
    )


# aceletation, fuel, fuel tank capacity
class Option(models.Model):
    name = models.CharField(max_length=70) 


# OPTIONVALUE > EQUIPMENT, OPTION
class OptionValue(models.Model):
    name = models.CharField(max_length=70) 
    equipment = models.ForeignKey(
        'Equipment',
        on_delete= models.CASCADE,
    )
    option = models.ForeignKey(
        'Option',
        on_delete= models.CASCADE,
    )
 

class Specification(models.Model):
    name = models.CharField(max_length=70) 


# SPECIFICATIONVALUE > TRIM, SPEFICIATION 
class SpecificationValue(models.Model):
    value = models.CharField(max_length=70)
    unit = models.CharField(max_length=70)
    trim = models.ForeignKey(
        'Trim',
        on_delete= models.CASCADE,
    )
    specification = models.ForeignKey(
        'Specification',
        on_delete= models.CASCADE,
    )


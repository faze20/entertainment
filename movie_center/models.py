from django.db import models
from django.conf  import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class MovieManagerPage(models.Model):
    GENERAL =  'G'
    PARENTAL_GUIDANCE = 'PG'
    THIRTEEN_PLUS = 'PG-13'

    RATINGS = [
        (GENERAL , ('General Audience')),
        (PARENTAL_GUIDANCE , ('PG')),
        (THIRTEEN_PLUS , ('PG-13')),
    ]

    ratings       =models.CharField(
        max_length=32,
        choices=RATINGS,
        default=GENERAL,
    )

    title         =  models.CharField(max_length=75)
    storyline     =  models.CharField(max_length=254)
    photo         = models.ImageField(upload_to='picture')
    web_url       = models.CharField(max_length=255)    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail',args=[str(self.id)])

    





# contact form module

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    message= models.TextField()


    def __str__(self):
        return self.query

    def get_absolute_url(self):
        return reverse('thankyou', args=[str(self.id)])




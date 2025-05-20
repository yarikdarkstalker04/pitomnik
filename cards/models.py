from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField("дата рождения")
    description = models.TextField()
    preview = models.ImageField(upload_to='gallery')

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='photos')


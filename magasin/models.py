from django.db import models

class Article(models.Model):
    libelle = models.CharField(max_length=100) 
    prix = models.FloatField()
    qte = models.IntegerField()
    dateAjout = models.DateField()
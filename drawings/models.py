from django.db import models

# Create your models here.
class Sketch(models.Model):
    img=models.ImageField(upload_to='pics')

class Samima(models.Model):
    img=models.ImageField(upload_to='picsofsamima')

class Tonima(models.Model):
    img=models.ImageField(upload_to='picsoftonima')
class Mithila(models.Model):
    img=models.ImageField(upload_to='picsofmithila')
class Isrita(models.Model):
    img=models.ImageField(upload_to='picsofisrita')
class Bintu(models.Model):
    img=models.ImageField(upload_to='picsofbintu')
class Puspo(models.Model):
    img=models.ImageField(upload_to='picsofpuspo')

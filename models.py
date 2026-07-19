from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class StaticProperty(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE) 
    shape = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    size = models.IntegerField()

    def __str__(self):
        return self.item.name


class DynamicProperty(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    direction = models.FloatField(default=0)
    length = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name
    
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'items',
]
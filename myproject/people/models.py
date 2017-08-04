from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    age = models.IntegerField()

    def __str__(self):
        return self.name + "  " + self.lastname

    def get_absolute_url(self):
        return reverse('people:detail', kwargs={"pk":self.pk})

from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    video = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def dump(self):
        return {"exercise":{'name':self.name,
                        'description':self.description,
                        'image':self.image,
                        'video':self.video,
                        'category':self.category.pk}}
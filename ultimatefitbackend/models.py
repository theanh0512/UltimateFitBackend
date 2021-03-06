from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)
    image = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Exercise(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    image2 = models.TextField()
    video = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def dump(self):
        create_on = self.created_datetime.strftime('%Y-%m-%d %H:%M:%S')
        modified_on = self.modified_datetime.strftime('%Y-%m-%d %H:%M:%S')
        return {"exercise": {'name': self.name,
                             'description': self.description,
                             'image': self.image,
                             'image2': self.image2,
                             'video': self.video,
                             'category': self.category.pk,
                             'modified_datetime': modified_on}}

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='courses')
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='course_category', on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.name
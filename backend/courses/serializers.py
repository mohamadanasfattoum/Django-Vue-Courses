from rest_framework import serializers
from .models import Course, Category

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
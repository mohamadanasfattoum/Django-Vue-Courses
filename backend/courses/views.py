from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import CourseFilter

from .serializers import CategorySerializers, CourseSerializers
from .models import Course, Category


class CourseListFilterAPI(generics.ListAPIView):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    filterset_class = CourseFilter


class CourseDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategorySerializers
    queryset = Course.objects.all()


class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


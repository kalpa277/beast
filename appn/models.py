from django.db import models
from rest_framework import serializers

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=90)
    Price=models.CharField(max_length=90)
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

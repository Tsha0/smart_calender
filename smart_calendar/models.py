from unicodedata import name
from django.db import models

class Lecture(models.Model):
    def __str__(self):
        return self.description
    description = models.CharField(max_length = 200)
    start_time = models.DateTimeField("Start Time:")
    end_time = models.DateTimeField("End Time:")

class Assignment(models.Model):
    def __str__(self):
        return self.assignment_description
    assigment_subject = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    due_date = models.DateTimeField("Due:")
    assignment_description = models.CharField(max_length = 200)

class Exam(models.Model):
    def __str__(self):
        return self.exam_description
    exam_subject = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    start_time = models.DateTimeField("Start Time:")
    end_time = models.DateTimeField("End Time:")
    exam_description = models.CharField(max_length = 200)
# Create your models here.

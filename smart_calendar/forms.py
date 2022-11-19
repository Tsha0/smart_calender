from socket import fromshare
from django import forms

class Lecture(forms.Form):
    description = forms.CharField(max_length = 200)
    start_time = forms.DateTimeField(label="Start_time")
    end_time = forms.DateTimeField(label="End_time")

class Assignment(forms.Form):
    due_date = forms.DateTimeField(label="Due:")
    assignment_description = forms.CharField(max_length = 200)

class Exam(forms.Form):
    start_time = forms.DateTimeField(label="Start_time:")
    end_time = forms.DateTimeField(label="End_time:")
    exam_description = forms.CharField(max_length = 200)
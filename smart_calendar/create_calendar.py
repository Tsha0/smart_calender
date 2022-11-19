from .models import Lecture,Assignment,Exam

def create_calendar():
    lecture = Lecture.objects.all()
    assignment = Assignment.objects.all()
    exam = Exam.objects.all()


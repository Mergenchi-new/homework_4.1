from django.shortcuts import render
from apps.nurai.models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', locals())
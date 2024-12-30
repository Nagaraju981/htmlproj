from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request, 'htmlapp/home.html')
    else:
        Student(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            mobno=request.POST.get('mobno'),
        ).save()
        return render(request, 'htmlapp/home.html')


    

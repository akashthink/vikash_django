from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    a=StudentRegistration()
    return render(request,'formss/userreg.html',{'form':a})
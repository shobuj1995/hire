from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.
def home(request):
	# data = user.objects.all()
	return render (request,'home.html')

def index(request):
	# data = user.objects.all()
	return render (request,'index.html')


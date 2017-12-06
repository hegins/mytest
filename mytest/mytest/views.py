#-*-coding:utf8-*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin(request):
	return render(request, 'admin.html')

def index(request):
	return render(request,'index.html')


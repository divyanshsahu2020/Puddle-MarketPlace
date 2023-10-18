from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import  login_required
# Create your views here.
from items.models import Item

@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,"dashboard_index.html",{'items':items})
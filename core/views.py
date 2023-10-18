from django.shortcuts import render,get_object_or_404,redirect
from items.models import Category,Item
from django.contrib.auth.models import User
from core import templates
from .forms import SignupForm
# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]

    categories=Category.objects.all()
    context={'items':items,'categories':categories}
    return render(request,"index.html",context)

def contact(request,*args,**kwargs):
    return render(request,"contact_page.html",{})
def signup(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    if request.method=="POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()

    return render(request,"signup.html",{'form':form})
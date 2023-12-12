from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def home(req): #1111111
    c = Course.objects.all()
    return render(req,'home.html',{'c':c}) 

def searches(req): #2222222
    form = Search1()
    if req.method == 'GET':
        form = Search1(req.GET)
        if form.is_valid():
            search = form.cleaned_data['search']    
            result = Course.objects.filter(id__icontains=search) or Course.objects.filter(name__icontains=search) #ค้นหาทั้ง id,name
        else:
            result = []
    else:
        form = Search1()
        result =[]
    return render(req,'result.html',{'result':result,'form':form})

def update(req,id):
    form = Update()
    c = Course.objects.get(pk=id)
    if req.method == 'POST':
        form = Update(req.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Update(instance=c)

    return render(req,'edit.html',{'form':form})

def delete(req):
    c = Course.objects.all()
    if req.method == 'POST':
        obj = req.POST.get('dlt')
        dlt = Course.objects.get(pk=obj)
        dlt.delete()
        return redirect('/')
    return render(req,'delete.html',{'c':c})
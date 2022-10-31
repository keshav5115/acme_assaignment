from django.shortcuts import render
from django.http import HttpResponse
from app1.models import user_model,department
from app1.form import departmentform,user_modelform
# Create your views here.

def create_department(request):
    data=departmentform()
    if request.method == 'POST':
        data=departmentform(request.POST)
        if data.is_valid():
            data.save()
        return HttpResponse('data is stord')
    return render(request,  'crud_depart.html', {'data':data})

def create_user_model(request):
    form=user_modelform()
    if request.method == 'POST':
        form=user_modelform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('data is stord')
    return render(request, 'create_user.html', {'form':form})
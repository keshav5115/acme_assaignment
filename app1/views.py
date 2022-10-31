from django.shortcuts import render
from django.http import HttpResponse

from app1.form import departmentform,user_modelform,Ticket_modelform
# Create your views here.

def Departmentview(request):
    data=departmentform()
    if request.method == 'POST':
        data=departmentform(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('data is stord')
    return render(request,  'crud_depart.html', {'data':data})

def User_modelview(request):
    form=user_modelform()
    if request.method == 'POST':
        form=user_modelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stord')
    return render(request, 'create_user.html', {'form':form})

def login(request):
    if request.method == 'POST':
        pass
    return  render(request, 'login_page.html')

def Ticketview(request):
    form=Ticket_modelform()
    if request.method == 'POST':
        form=Ticket_modelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stord')
    return render(request,'ticket.html',{'form':form})
        

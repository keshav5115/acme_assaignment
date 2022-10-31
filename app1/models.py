from random import choices
from django.db import models

# Create your models here.
class Department(models.Model):
    did=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    description=models.TextField()
    created_by=models.CharField(max_length=40)
    created_at=models.CharField(max_length=40)
    last_updated=models.DateTimeField(auto_now_add=True)

class User_model(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.PositiveBigIntegerField()
    password=models.CharField(max_length=40)
    created_by=models.CharField(max_length=40)
    created_at=models.CharField(max_length=40)
    last_updated=models.DateTimeField(auto_now_add=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


class Ticket_model(models.Model):
    ticket_id = models.CharField(primary_key=True,max_length=20)
    subject=models.CharField(max_length=40)
    body=models.TextField()
    priority=models.CharField(max_length=20,choices=[[]])
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
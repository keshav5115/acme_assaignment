from enum import auto
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Department(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    created_by = models.CharField(max_length=40)
    created_at = models.TimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)


phone_validator = RegexValidator(
    r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class User_model(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, validators=[
                             phone_validator], unique=True)
    password = models.CharField(max_length=40)
    created_by = models.CharField(max_length=40)
    created_at = models.CharField(max_length=40)
    last_updated = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    REQUIRED_FIELDS = ["phone", "email"]


class Ticket_model(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=20)
    subject = models.CharField(max_length=40)
    body = models.TextField()
    priority = models.CharField(max_length=20, choices=[])
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()

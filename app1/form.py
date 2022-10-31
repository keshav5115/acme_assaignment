from pyexpat import model
from django import forms

from app1.models import Department,User_model,Ticket_model


class Departmentform(forms.modelsForm):
    class Meta:
        model=Department
        fields='__all__'

class User_modelform(forms.modelsForm):
    class Meta:
        model=User_model
        fields='__all__'

class Ticket_modelform(forms.modelsForm):
    class Meta:
        model=Ticket_model
        fields='__all__'
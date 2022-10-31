from pyexpat import model
from django import forms

from app1.models import department,user_model


class departmentform(forms.modelsForm):
    class Meta:
        model=department
        fields='__all__'

class user_modelform(forms.modelsForm):
    class Meta:
        model=user_model
        fields='__all__'
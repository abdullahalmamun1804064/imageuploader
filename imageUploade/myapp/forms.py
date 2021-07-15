from django import forms
from django.db import models
from django.forms import fields
from .models import image_model

class image_from(forms.ModelForm):
    class Meta:
        model=image_model
        fields='__all__'
        labels={'photo':''}
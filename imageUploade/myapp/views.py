from django.shortcuts import render
from .models import image_model
from .forms import image_from

# Create your views here.
def home(request):
    if request.method=="POST":
        fm=image_from(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    fm=image_from()
    image=image_model.objects.all()
    dic={
        'form':fm,
        'img':image,
    }
        
    return render(request,'myapp/home.html',dic)
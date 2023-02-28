from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     ab=x-y
#     bc=x*y
#     cd=x/y
#     return render(request,"calculate.html",{'addt':res,'subb':ab,'mul':bc,'div':cd})



# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("im contact")
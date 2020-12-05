from django.shortcuts import render

# Create your views here.
def order(request):
    list={}
    return render(request,'cart.html',list)




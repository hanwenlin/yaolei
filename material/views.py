from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Meterials

# Create your views here.
def index(request):
    materials = Meterials.objects.all()
    return render(request,'material/index.html',{"materials":materials})

def delete(request,meterid):
    Meterials.objects.get(id=meterid).delete()
    return redirect(reverse('material:index',args=()))

def search(request):
    search_name = request.POST.get('search')

    materials = Meterials.objects.filter(meterialType=search_name)

    # return HttpResponse('okk')
    return render(request,'material/index.html',{"materials":materials})
def addtion(request):
    pass

def modifys(request):
    pass
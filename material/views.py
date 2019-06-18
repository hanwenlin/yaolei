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
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        meterialName = clean_data.get('meterialName')
        meterialType = clean_data.get('meterialType')
        brand = clean_data.get('brand')
        matrix = clean_data.get('matrix')
        ligand = clean_data.get('ligand')
        diameter = clean_data.get('diameter')
        tolePressure = clean_data.get('tolePressure')
        phRange = clean_data.get('phRange')
        storeMethod = clean_data.get('storeMethod')
        comFactor = clean_data.get('comFactor')
        dbc = clean_data.get('dbc')
        capacityRange = clean_data.get('capacityRange')
        velocityPressure = clean_data.get('velocityPressure')
        validtyPeriod = clean_data.get('validtyPeriod')
        packingMethod = clean_data.get('packingMethod')
        packingdetail = clean_data.get('packingdetail')
        Meterials.objects.create(meterialName=meterialName,meterialType=meterialType,brand=brand,
                                 matrix=matrix,ligand=ligand,diameter=diameter,tolePressure=tolePressure,
                                 phRange=phRange,storeMethod=storeMethod,comFactor=comFactor,dbc=dbc,
                                 capacityRange=capacityRange,velocityPressure=velocityPressure,validtyPeriod=validtyPeriod,
                                 packingMethod=packingMethod,packingdetail=packingdetail)
        # return render(request, 'material/addition.html')
        return redirect(reverse('material:index', args=()))

    return render(request, 'material/addition.html')


def modifys(request,meterid):
    material = Meterials.objects.get(id=meterid)
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        meterialName = clean_data.get('meterialName')
        meterialType = clean_data.get('meterialType')
        brand = clean_data.get('brand')
        matrix = clean_data.get('matrix')
        ligand = clean_data.get('ligand')
        diameter = clean_data.get('diameter')
        tolePressure = clean_data.get('tolePressure')
        phRange = clean_data.get('phRange')
        storeMethod = clean_data.get('storeMethod')
        comFactor = clean_data.get('comFactor')
        dbc = clean_data.get('dbc')
        capacityRange = clean_data.get('capacityRange')
        velocityPressure = clean_data.get('velocityPressure')
        validtyPeriod = clean_data.get('validtyPeriod')
        packingMethod = clean_data.get('packingMethod')
        packingdetail = clean_data.get('packingdetail')
        Meterials.objects.filter(id=meterid).update(meterialName=meterialName,meterialType=meterialType,brand=brand,
                                 matrix=matrix,ligand=ligand,diameter=diameter,tolePressure=tolePressure,
                                 phRange=phRange,storeMethod=storeMethod,comFactor=comFactor,dbc=dbc,
                                 capacityRange=capacityRange,velocityPressure=velocityPressure,validtyPeriod=validtyPeriod,
                                 packingMethod=packingMethod,packingdetail=packingdetail)
        return redirect(reverse('material:index', args=()))
    return render(request,'material/modiftion.html',{"material":material})
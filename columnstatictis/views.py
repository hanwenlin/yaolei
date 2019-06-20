from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Columnstatictis
from material.models import  Meterials

# Create your views here.
def index(request):
    columns = Columnstatictis.objects.all()
    return render(request,'columnstatictis/index.html',{"columns":columns})

def delete(request,columnid):
    Columnstatictis.objects.get(id=columnid).delete()
    return redirect(reverse('columnstatictis:index',args=()))

def search(request):
    search_name = request.POST.get('search_column')
    print(search_name)
    resinid = Meterials.objects.get(meterialName=search_name).id
    columns = Columnstatictis.objects.filter(resin_id=resinid)

    return render(request,'columnstatictis/index.html',{"columns":columns})

def addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        resin = clean_data.get('resin')
        packingitem = clean_data.get('packingitem')
        histcode = clean_data.get('histcode')
        resincode = clean_data.get('resincode')
        lowestspeed = clean_data.get('lowestspeed')
        hightspeed = clean_data.get('hightspeed')
        pressure = clean_data.get('pressure')
        yieldspeed = clean_data.get('yieldspeed')
        columnheight = clean_data.get('columnheight')
        columndimeter = clean_data.get('columndimeter')
        symmetry = clean_data.get('symmetry')
        hetp = clean_data.get('hetp')
        comment = clean_data.get('comment')
        resin_id = Meterials.objects.get(meterialName=resin).id
        # Columnstatictis.objects.create(meterialName=meterialName,meterialType=meterialType,brand=brand,
        #                          matrix=matrix,ligand=ligand,diameter=diameter,tolePressure=tolePressure,
        #                          phRange=phRange,storeMethod=storeMethod,comFactor=comFactor,dbc=dbc,
        #                          capacityRange=capacityRange,velocityPressure=velocityPressure,validtyPeriod=validtyPeriod,
        #                          packingMethod=packingMethod,packingdetail=packingdetail)
        # return render(request, 'material/addition.html')
        Columnstatictis.objects.create(packingitem=packingitem,histcode=histcode,resincode=resincode,lowestspeed=lowestspeed,
                                       hightspeed=hightspeed,pressure=pressure,yieldspeed=yieldspeed,columnheight=columnheight,
                                       columndimeter=columndimeter,symmetry=symmetry,hetp=hetp,comment=comment,resin_id=resin_id)
        return redirect(reverse('columnstatictis:index', args=()))

    return render(request, 'columnstatictis/addition.html')


def modifys(request,columnid):
    column = Columnstatictis.objects.get(id=columnid)
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        clean_data = request.POST
        # clean_data = request.POST
        resin = clean_data.get('resin')
        packingitem = clean_data.get('packingitem')
        histcode = clean_data.get('histcode')
        resincode = clean_data.get('resincode')
        lowestspeed = clean_data.get('lowestspeed')
        hightspeed = clean_data.get('hightspeed')
        pressure = clean_data.get('pressure')
        yieldspeed = clean_data.get('yieldspeed')
        columnheight = clean_data.get('columnheight')
        columndimeter = clean_data.get('columndimeter')
        symmetry = clean_data.get('symmetry')
        hetp = clean_data.get('hetp')
        comment = clean_data.get('comment')
        resin_id = Meterials.objects.get(meterialName=resin).id
        # Columnstatictis.objects.filter(id=columnid).update(meterialName=meterialName,meterialType=meterialType,brand=brand,
        #                          matrix=matrix,ligand=ligand,diameter=diameter,tolePressure=tolePressure,
        #                          phRange=phRange,storeMethod=storeMethod,comFactor=comFactor,dbc=dbc,
        #                          capacityRange=capacityRange,velocityPressure=velocityPressure,validtyPeriod=validtyPeriod,
        #                          packingMethod=packingMethod,packingdetail=packingdetail)
        Columnstatictis.objects.filter(id=columnid).update(packingitem=packingitem,histcode=histcode,resincode=resincode,lowestspeed=lowestspeed,
                                       hightspeed=hightspeed,pressure=pressure,yieldspeed=yieldspeed,columnheight=columnheight,
                                       columndimeter=columndimeter,symmetry=symmetry,hetp=hetp,comment=comment,resin_id=resin_id)
        return redirect(reverse('columnstatictis:index', args=()))
    return render(request,'columnstatictis/modiftion.html',{"column":column})
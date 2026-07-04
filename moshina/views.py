from django.shortcuts import render,redirect
from moshina.models import Moshina
# Create your views here.
def moshina_list(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi','').strip()
        if nomi:
            Moshina.objects.create(
                nomi=nomi
            )
            return redirect('moshina_list')
    car = Moshina.objects.all()
    context = {
        'car': car
    }
    return render(request, 'moshina.html',context=context)

def moshina_edit(request, id):
    car = Moshina.objects.get(id=id)
    if request.method == 'POST':
        nomi = request.POST.get('nomi', '').strip()
        if nomi:
            car.nomi = nomi
            car.save()
            return redirect('moshina_list')
    cars = Moshina.objects.all()
    
    context = {
        'carr':car,
        'car':cars,
    }
    return render(request, 'moshina.html', context=context)
    
def moshina_delete(request,id):
    print('ociriwga ruxsat keldi..',id)
    Moshina.objects.get(id=id).delete()
    return redirect('moshina_list')
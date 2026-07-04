from django.shortcuts import render,redirect
from telefon.models import Phone
# Create your views here.
def telefon_list(request):
    if request.method =='POST':
        nomi = request.POST.get('nomi','').strip()
        if nomi:
            Phone.objects.create(
                nomi=nomi
            )
            return redirect('telefon_list')
    phone = Phone.objects.all()
    context = {
        'phone':phone
    }
    return render(request, 'telefon.html', context=context)


def telefon_edit(request, id):
    tel = Phone.objects.get(id=id)
    if request.method == 'POST':
        nomi = request.POST.get('nomi', '').strip()
        if nomi:
            tel.nomi = nomi
            tel.save()
            return redirect('telefon_list')
    phones = Phone.objects.all()
    
    context = {
        'tel': tel,
        'phone': phones,
    }
    return render(request, 'telefon.html', context=context)


def telefon_delete(request,id):    
    print('ociriwga sorovkeldi..',id)
    Phone.objects.get(id=id).delete()
    return redirect('telefon_list')

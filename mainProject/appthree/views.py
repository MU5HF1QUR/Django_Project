from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . forms import suggestForm, ContactForm
from . models import suggestInfo, contactInfo

# Create your views here.

def aThree(request):
    return render(request, 'appThree/three.html')

def char(request):
    return render(request, 'appThree/char.html')

def aSite(request):
    return render(request, 'appThree/aSite.html')

def mSite(request):
    return render(request, 'appThree/mSite.html')

def contactUs(request):
    frm = ContactForm(request.POST)
    if frm.is_valid():
        tname = frm.cleaned_data['name']
        temail = frm.cleaned_data['email']
        tphone = frm.cleaned_data['phone']
        tmessage = frm.cleaned_data['message']

        addToModel = contactInfo(name = tname, email = temail, phone = tphone, message = tmessage)
        addToModel.save()

        return HttpResponseRedirect('/three/sgtSucces/')
    
    return render(request, 'appThree/cUs.html', {'form':frm})

def sgt(request):
    frm = suggestForm(request.POST, label_suffix=' :' )
    frm.order_fields(field_order=['type', 'name', 'rating', 
    'description'])
    if frm.is_valid():
            ttype = frm.cleaned_data['type']
            tname = frm.cleaned_data['name']
            trating = frm.cleaned_data['rating']
            tdescription = frm.cleaned_data['description']

            addToModel = suggestInfo(name = tname, rating = trating, description = tdescription, type = ttype)
            addToModel.save()

            return HttpResponseRedirect('/three/sgtSucces/')
    
    return render(request, 'appThree/sgt.html', {'form':frm})

def success1(request):
    return render(request, 'appThree/succes.html')
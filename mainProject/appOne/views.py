from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm, SetPasswordForm
from . forms import usercf
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.

def aOne (request):
    a1 = 'App one feature 1'
    a2 = 'App one feature 2'
    a3 = 'App one feature 3'
    a4 = 'App one feature 4'
    a_dict = {'f1' : a1, 'f2' : a2, 'f3' : a3, 'f4' : a4,}
    
    return render(request, 'appOne/one.html',  a_dict)

def tFeature (request):
    return render(request, 'appOne/totalFeature.html',  {'d_val': 4, 'feature':'four'})

def nav (request):
    return render(request, 'appOne/pMain.html')

# user creation/ registration
def usercform(request):
    if request.method == "POST":
        frm = usercf(request.POST)
        if frm.is_valid():
            messages.success(request, 'Succesfully Registerd!')
            frm.save()
            
    else:
        frm = usercf()
    return render(request, 'appOne/userCForm.html', {'form':frm})


# Login
def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/success')
    else:
        frm = AuthenticationForm()
    return render(request, 'appOne/login.html', {'form':frm})


#Successfully login
def slogin(request):
    return render(request, 'appOne/pMain.html')


#Logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')


#using old pass

def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = PasswordChangeForm(user=request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/')
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request, 'appOne/cPass.html', {'form':frm})
    else:
        return HttpResponseRedirect('/')
    

#using without old pass

def without_old_password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = SetPasswordForm(user=request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/')
        else:
            frm = SetPasswordForm(user=request.user)
        return render(request, 'appOne/cPassWithout.html', {'form':frm})
    else:
        return HttpResponseRedirect('/')
from django.urls import path
from . import views

urlpatterns = [
    path('',views.aThree),
    path('ch/',views.char, name='char'),
    path('aS/',views.aSite, name='aSite'),
    path('mS/',views.mSite, name='mSite'),
    path('cUS/',views.contactUs, name='contact'),
    path('sg_form/',views.sgt, name='suggest'),
    path('sgtSucces/',views.success1, name='Succes'),
]
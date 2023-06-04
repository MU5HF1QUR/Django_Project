from django.urls import path
from . import views

urlpatterns = [
    path('',views.aTwo),
    path('srs/',views.srs, name='series'),
    path('mvs/',views.mov, name='movies'),
]
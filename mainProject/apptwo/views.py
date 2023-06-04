from django.shortcuts import render
from apptwo.models import movies, series
# Create your views here.

def aTwo(request):
    dev_info = {'di': ['Mushfiqur Rahman', 'Batch-2', 'Doing Django']}
    return render(request, 'appTwo/two.html', dev_info)


def mov(request):
    mDetails = movies.objects.all()
    return render(request, 'appTwo/movies.html', {'mov':mDetails})

def srs(request):
    sDetails = series.objects.all()
    return render(request, 'appTwo/series.html', {'srs':sDetails})
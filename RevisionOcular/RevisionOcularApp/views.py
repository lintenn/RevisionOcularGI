from django.shortcuts import render, HttpResponse
from RevisionOcularApp.models import tClient,tEye 

# Create your views here.

def home(request):

    clientes = tClient.objects.all()

    return render(request, "RevisionOcularApp/home.html" , {"clientes":clientes})

def revision(request):

    return render(request, "RevisionOcularApp/revision.html")



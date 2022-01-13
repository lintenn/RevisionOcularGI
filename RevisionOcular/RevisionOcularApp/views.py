from django.shortcuts import render, HttpResponse
from RevisionOcularApp.models import tClient,tEye

# Create your views here.

def home(request):

    clientes = tClient.objects.all()

    return render(request, "RevisionOcularApp/home.html" , {"clientes":clientes, "range":range(1,100)})

def revision(request):

    revisiones = tEye.objects.all()

    return render(request, "RevisionOcularApp/revision.html", {"revisiones":revisiones})



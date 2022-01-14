from django.shortcuts import render, HttpResponse
from RevisionOcularApp.models import tClient,tEye

# Create your views here.

def home(request):

    clientes = tClient.objects.all()

    return render(request, "RevisionOcularApp/home.html" , {"clientes":clientes, "range":range(1,100)})

def clientselect(request, NIF):

    clientes = tClient.objects.all()

    cliente = tClient.objects.get(NIF = NIF)

    return render(request, "RevisionOcularApp/clientselect.html", {"clientes":clientes, "range":range(1,100), "cliente":cliente})

def revision(request, NIF):

    revisiones = tEye.objects.filter(NIF = NIF)

    cliente = tClient.objects.get(NIF = NIF)

    return render(request, "RevisionOcularApp/revision.html", {"revisiones":revisiones, "cliente":cliente})

def revisionselect(request, NIF, id):

    revisiones = tEye.objects.filter(NIF = NIF)

    revision = tEye.objects.get(id = id)

    cliente = tClient.objects.get(NIF = NIF)

    return render(request, "RevisionOcularApp/revisionselect.html", {"revisiones":revisiones, "revision":revision, "cliente":cliente})


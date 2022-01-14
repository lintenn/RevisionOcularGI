from django.shortcuts import render, HttpResponse, redirect
from RevisionOcularApp.models import tClient,tEye

# Create your views here.


def home(request):

    clientes = tClient.objects.all()

    return render(request, "RevisionOcularApp/home.html" , {"clientes":clientes, "range":range(1,100)})


def clientselect(request, NIF):

    if request.method == "POST":
        nif = request.POST.get("nif")
        nombre = request.POST.get("nombre")
        apellidos = request.POST.get("apellidos")
        edad = request.POST.get("edad")
        if request.POST.get("bAdd") is not None:
            c = tClient(NIF=nif, NOMBRE=nombre, APELLIDO=apellidos, EDAD=edad)
            c.save()

        elif request.POST.get("bUpd") is not None:
            c = tClient.objects.get(NIF=NIF)
            c.NIF = nif
            c.NOMBRE = nombre
            c.APELLIDO = apellidos
            c.EDAD = edad
            c.save()

        elif request.POST.get("bDel") is not None:
            c = tClient.objects.get(NIF=nif)
            c.delete()

        return redirect("http://127.0.0.1:8000/")

    clientes = tClient.objects.all()

    cliente = tClient.objects.filter(NIF=NIF).first()

    return render(request, "RevisionOcularApp/clientselect.html", {"clientes":clientes, "range":range(1,100), "cliente":cliente})


def revision(request, NIF):

    revisiones = tEye.objects.filter(NIF=NIF)

    cliente = tClient.objects.get(NIF=NIF)

    return render(request, "RevisionOcularApp/revision.html", {"revisiones":revisiones, "cliente":cliente})


def revisionselect(request, NIF, id):

    revisiones = tEye.objects.filter(NIF=NIF)

    revision = tEye.objects.get(id=id)

    cliente = tClient.objects.get(NIF=NIF)

    return render(request, "RevisionOcularApp/revisionselect.html", {"revisiones":revisiones, "revision":revision, "cliente":cliente})


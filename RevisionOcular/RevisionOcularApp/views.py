from django.shortcuts import render, HttpResponse, redirect
from RevisionOcularApp.models import tClient,tEye

# Create your views here.


def home(request):

    if request.method == "POST":
        nif = request.POST.get("nif")
        nombre = request.POST.get("nombre")
        apellidos = request.POST.get("apellidos")
        edad = request.POST.get("edad")
        if request.POST.get("bAdd") is not None and nif != "":
            c = tClient(NIF=nif, NOMBRE=nombre, APELLIDO=apellidos, EDAD=edad)
            c.save()

        return redirect("http://127.0.0.1:8000/")

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
            c = tClient.objects.filter(NIF=NIF).first()
            if c.NIF != nif:
                c_new = tClient(NIF=nif, NOMBRE=nombre, APELLIDO=apellidos, EDAD=edad)
                c_new.save()
                for r in tEye.objects.filter(NIF=c):
                    r.NIF = c_new
                    r.save()
                    c.delete()
                return redirect("http://127.0.0.1:8000/")

            if c.NOMBRE != nombre:
                c.NOMBRE = nombre    
            if c.APELLIDO != apellidos:
                c.APELLIDO = apellidos
            if c.EDAD != edad:
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

    cliente = tClient.objects.get(NIF=NIF)

    if request.method == "POST":
        oesfera = request.POST.get("oesfera")
        iesfera = request.POST.get("iesfera")
        ocilindro = request.POST.get("ocilindro")
        icilindro = request.POST.get("icilindro")
        oadicion = request.POST.get("oadicion")
        iadicion = request.POST.get("iadicion")
        oagudeza = request.POST.get("oagudeza")
        iagudeza = request.POST.get("iagudeza")
        consulta = request.POST.get("consulta")

        if request.POST.get("bAdd") is not None:
            r = tEye(NIF=cliente, CONSULTA=consulta, OD_ESFERA=oesfera, OD_CILINDRO=ocilindro, OD_ADICION=oadicion,
                OD_AGUDEZA=oagudeza, OI_ESFERA=iesfera, OI_CILINDRO=icilindro, OI_ADICION=iadicion, OI_AGUDEZA=iagudeza)
            r.save()

        return redirect("http://127.0.0.1:8000/{}/revision/".format(cliente.NIF))

    revisiones = tEye.objects.filter(NIF=NIF)

    return render(request, "RevisionOcularApp/revision.html", {"revisiones":revisiones, "cliente":cliente})


def revisionselect(request, NIF, id):

    cliente = tClient.objects.get(NIF=NIF)

    if request.method == "POST":
        oesfera = request.POST.get("oesfera")
        iesfera = request.POST.get("iesfera")
        ocilindro = request.POST.get("ocilindro")
        icilindro = request.POST.get("icilindro")
        oadicion = request.POST.get("oadicion")
        iadicion = request.POST.get("iadicion")
        oagudeza = request.POST.get("oagudeza")
        iagudeza = request.POST.get("iagudeza")
        consulta = request.POST.get("consulta")

        if request.POST.get("bAdd") is not None:
            r = tEye(NIF=cliente, CONSULTA=consulta, OD_ESFERA=oesfera, OD_CILINDRO=ocilindro, OD_ADICION=oadicion,
                OD_AGUDEZA=oagudeza, OI_ESFERA=iesfera, OI_CILINDRO=icilindro, OI_ADICION=iadicion, OI_AGUDEZA=iagudeza)
            r.save()

        elif request.POST.get("bUpd") is not None:
            r = tEye.objects.filter(id=id).first()

            if r.CONSULTA != consulta:
                r.CONSULTA = consulta    
            if r.OD_ESFERA != oesfera:
                r.OD_ESFERA = oesfera
            if r.OD_CILINDRO != ocilindro:
                r.OD_CILINDRO = ocilindro
            if r.OD_ADICION != oadicion:
                r.OD_ADICION = oadicion
            if r.OD_AGUDEZA != oagudeza:
                r.OD_AGUDEZA = oagudeza
            if r.OI_ESFERA != iesfera:
                r.OI_ESFERA = iesfera
            if r.OI_CILINDRO != icilindro:
                r.OI_CILINDRO = icilindro
            if r.OI_ADICION != iadicion:
                r.OI_ADICION = iadicion
            if r.OI_AGUDEZA != iagudeza:
                r.OI_AGUDEZA = iagudeza
            r.save()

        elif request.POST.get("bDel") is not None:
            r = tEye.objects.get(id=id)
            r.delete()

        return redirect("http://127.0.0.1:8000/{}/revision/".format(cliente.NIF))

    revisiones = tEye.objects.filter(NIF=NIF)

    revision = tEye.objects.get(id=id)

    return render(request, "RevisionOcularApp/revisionselect.html", {"revisiones":revisiones, "revision":revision, "cliente":cliente})


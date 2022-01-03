from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "RevisionOcularApp/home.html")

def revision(request):

    return render(request, "RevisionOcularApp/revision.html")

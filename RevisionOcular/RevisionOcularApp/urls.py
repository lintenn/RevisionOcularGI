# URLs propias de la aplicación RevisionOcularApp y que serán incluidas en las URLs del proyecto general RevisionOcular
from django.urls import path

from RevisionOcularApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('revision', views.revision, name="Revision"),
]
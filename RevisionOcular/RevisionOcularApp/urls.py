# URLs propias de la aplicación RevisionOcularApp y que serán incluidas en las URLs del proyecto general RevisionOcular
from django.urls import path

from RevisionOcularApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('<NIF>/', views.clientselect, name="clientselect"),
    path('<NIF>/revision/', views.revision, name="Revision"),
    path('<NIF>/revision/<int:id>/', views.revisionselect, name="revisionselect")
]
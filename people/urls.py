from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.PersonListView.as_view()),
    path("people/create/", views.CreatePerson.as_view()),
    path("people/detail/<int:pk>/", views.RetrieveUpdateDestroyPerson.as_view()),
]

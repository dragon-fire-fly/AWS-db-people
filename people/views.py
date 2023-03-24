from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Person
from .serializers import PersonSerializer


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CreatePerson(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RetrieveUpdateDestroyPerson(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from frontend.models import users
from .serializers import DataSerializer

class DataListView(ListAPIView):
    queryset=users.objects.all()
    serializer_class=DataSerializer

class DataDetailView(RetrieveAPIView):
    queryset=users.objects.all()
    serializer_class=DataSerializer

class DataCreateView(CreateAPIView):
    queryset=users.objects.all()
    serializer_class=DataSerializer

class DataUpdateView(UpdateAPIView):
    queryset=users.objects.all()
    serializer_class=DataSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import PermintaanIkan
from .serializers import PermintaanIkanSerializer
from .utils import weighted_moving_average
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class PermintaanIkanViewSet(viewsets.ModelViewSet):
    queryset = PermintaanIkan.objects.all()
    serializer_class = PermintaanIkanSerializer

@api_view(['GET'])
def prediksi_permintaan(request):
    permintaan = PermintaanIkan.objects.order_by('-tanggal')[:5]  # Ambil 5 data terakhir
    serializer = PermintaanIkanSerializer(permintaan, many=True)
    data = [item['jumlah'] for item in serializer.data]
    weights = [1, 2, 3, 4, 5]
    prediksi = weighted_moving_average(data, weights)
    return Response({'prediksi': prediksi})


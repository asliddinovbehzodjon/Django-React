from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu,Mahsulot
from .serializer import MenuSerializer,MahsulotSerializer
class AllMenu(APIView):
    def get(self,request):
        all=Menu.objects.all()
        serializer=MenuSerializer(all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class AllMahsulot(APIView):
    def get(self,request):
        all=Mahsulot.objects.all()
        serializer=MahsulotSerializer(all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
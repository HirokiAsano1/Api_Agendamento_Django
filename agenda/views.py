from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class AgendamentoDetail(APIView):
    def get (self,request,id):
        obj = get_object_or_404(Agendamento, id = id) # busa o obj no banco pelo id
        serializer = AgendamentoSerializer(obj) #transformas os campos dos obj em Json
        return JsonResponse(serializer.data)
    
    def patch(self,request,id):
        obj = get_object_or_404(Agendamento, id = id) # busa o obj no banco pelo id
        serializer = AgendamentoSerializer(obj, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()# metodo padrao criado pelo djangoRest             
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors, status=400)
    
    def delete(self,request,id):
        obj = get_object_or_404(Agendamento, id = id) # busa o obj no banco pelo id
        obj.delete()
        return Response(status=204)

class AgendamentoList(APIView):
    def get(self,request):
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self,request):
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # metodo padrao criado pelo djangoRest
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 404)


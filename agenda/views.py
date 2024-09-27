from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(http_method_names=["GET","PATCH","DELETE"])
def agendamento_details(request , id):
    obj = get_object_or_404(Agendamento, id = id) # busa o obj no banco pelo id
    if request.method == "GET":
        serializer = AgendamentoSerializer(obj) #transformas os campos dos obj em Json
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        serializer = AgendamentoSerializer(obj, data=request.data, partial =True) #se for passado no parametro do serializer obj e data , o metodo ira puxar seriliazer update
        if serializer.is_valid():
            serializer.save()# metodo padrao criado pelo djangoRest             
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":     
        obj.delete()
        return Response(status=204)



@api_view(http_method_names=["GET","POST"])
def agendamento_list(request):
    if request.method == "GET":
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save() # metodo padrao criado pelo djangoRest
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 404)

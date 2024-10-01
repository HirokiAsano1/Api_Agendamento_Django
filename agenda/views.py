from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer , PrestadorSerializer
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from datetime import datetime
from agenda.utils import get_horarios_disponiveis

# Create your views here.

class isOwnerorCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username = request.query_params.get("username", None)
        if request.user.username == username:
            return True
        return False

class IsPrestador(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
         if obj.prestador == request.user:
             return True
         return False

class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView): #os metodos de Get(id) , Update , Destroy incluidos  nesse generic
    permission_classes = [IsPrestador]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
class AgendamentoList(generics.ListCreateAPIView): #os metodo do crud get(all) e post ja estao incluidos nesse generic  
                                                    #/api/agendamentos/?username=hirok              
    serializer_class = AgendamentoSerializer
    permission_classes = [isOwnerorCreateOnly]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Agendamento.objects.filter(prestador__username=username)
        return queryset
    
class PrestadorList(generics.ListAPIView): #Listar os Prestadores de Seriços          
    serializer_class = PrestadorSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
        

@api_view(http_method_names=["GET"])
def get_horarios(request):
    data = request.query_params.get("data")
    
    if not data:
        data = datetime.now().date()  # Se nenhum valor for passado, usa a data atual
    else:
        try:
            data = datetime.fromisoformat(data).date()  # Tenta converter a string para data
        except ValueError:
            return JsonResponse({'error': 'Data inválida, use o formato YYYY-MM-DD'}, status=400)

    horarios_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return JsonResponse(horarios_disponiveis, safe=False)
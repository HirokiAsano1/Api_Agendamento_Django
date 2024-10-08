from rest_framework import serializers
from agenda.models import Agendamento
from django.utils import timezone
from django.contrib.auth.models import User


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Agendamento
         fields = ['id','data_horario','nome_cliente','email_cliente','telefone_cliente','prestador'] 
         
    prestador = serializers.CharField()
    def validate_prestador(self,value): 
          try:
               prestador_obj = User.objects.get(username=value)
          except User.DoesNotExist:
               raise serializers.ValidationError("Username nâo existe")
          return prestador_obj 

    def validate_data_horario(self, value):
        if value <timezone.now():
             raise serializers.ValidationError("Agendamento Não pode ser feito no passado!")
        return value
    
    def validate(self, attrs):
         telefone_cliente = attrs.get("telefone_cliente","")
         email_Cliente = attrs.get("email_cliente","")

         if email_Cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_cliente.startswith("+55"):
              raise serializers.ValidationError("E-mail brasileiro deve estar associado a um número do Brasil(+55)")
         return attrs

class PrestadorSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id', 'username', 'agendamentos']

     agendamentos = AgendamentoSerializer(many=True,read_only =True)
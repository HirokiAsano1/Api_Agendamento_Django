from rest_framework.test import APITestCase
import json
from agenda.models import Agendamento
from datetime import datetime , timezone
# Create your tests here.

class TestListagemAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(
            data_horario = datetime(2022, 3, 15 , tzinfo=timezone.utc),
            nome_cliente ="Alice",
            email_cliente = "alice@gmail.com",
            telefone_cliente = "9999219129",
        )

        agendamento_serializado = {
            "id":1,
            "data_horario": "2022-03-15T00:00:00Z",
            "nome_cliente": "Alice",
            "email_cliente": "alice@gmail.com",
            "telefone_cliente": "9999219129",
        }
        
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertDictEqual(data[0], agendamento_serializado)

class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_request_data = {
            "data_horario": "2025-03-15T00:00:00Z",
            "nome_cliente": "Alice",
            "email_cliente": "alice@gmail.com",
            "telefone_cliente": "9999219129",
        }

        response = self.client.post("/api/agendamentos/", agendamento_request_data, format="json")
        agendamento_criado = Agendamento.objects.get()
        # Obtendo o agendamento recém-criado
        self.assertEqual(agendamento_criado.data_horario, datetime(2025, 3, 15, tzinfo=timezone.utc))
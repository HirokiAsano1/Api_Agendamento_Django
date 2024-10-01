from typing import Iterable
from datetime import date , datetime , timedelta,timezone

from agenda.models import Agendamento

def get_horarios_disponiveis(data:date) -> Iterable[datetime]:
    start = datetime(year=data.year, month=data.month, day = data.day , hour=9,minute=0,tzinfo=timezone.utc)
    end = datetime(year=data.year, month=data.month, day = data.day , hour=18,minute=0,tzinfo=timezone.utc)
    delta = timedelta(hours=1)
    horarios_disponiveis =set()
    while start < end:
        if not Agendamento.objects.filter(data_horario =start).exists():
            horarios_disponiveis.add(start)
        start = start + delta
    
    return horarios_disponiveis
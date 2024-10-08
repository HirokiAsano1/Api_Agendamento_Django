FROM python:3.10-slim-buster

# Instala dependências do sistema necessárias para o PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev

# Definindo o diretório de trabalho
WORKDIR /app

COPY requirements.txt /app/

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . /app/

# Definindo o comando para iniciar o servidor Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# API de Agendamento de Serviços

Esta é uma API Restful desenvolvida utilizando Django, DjangoRest, Postgres e Docker, com o objetivo de realizar agendamentos de serviços. A API permite cadastrar prestadores de serviços (gerenciados pelo sistema de usuários do Django), bem como informações dos clientes e horários dos agendamentos. 

## Funcionalidades

- **CRUD de Agendamentos:** Cadastro de serviços agendados com nome do cliente, e-mail, telefone, prestador e data/hora.
- **Listagem de Prestadores:** Listar os prestadores de serviços cadastrados.
- **Listagem de Horários Disponíveis:** Retornar horários disponíveis para um prestador específico.
- **Autenticação e Permissões:** Apenas prestadores podem visualizar, atualizar ou deletar seus próprios agendamentos.

## Requisitos

- Python 3.8+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker (para execução em containers)

## Instalação e Execução

### 1. Clone o repositório

```bash
git clone [https://github.com/seuusuario/nome-do-repositorio.git](https://github.com/HirokiAsano1/Api_Agendamento_Django) 
```
### 2. Executar com Docker

Utilize o Docker para rodar o projeto localmente.

```bash
docker-compose up --build
```

### 3. Criar um Superusuário

Para acessar o painel de administração do Django, crie um superusuário:

```bash
docker-compose exec web python manage.py createsuperuser
```

## 4. Acessar a API

A API estará disponível em `http://localhost:8000/`.

Você pode acessar o painel de administração do Django em `http://localhost:8000/admin/`.

## Endpoints da API

- `GET /agendamentos/` - Lista os agendamentos de um prestador específico.
- `POST /agendamentos/` - Cria um novo agendamento.
- `GET /agendamentos/{id}` - Retorna os detalhes de um agendamento específico.
- `PUT /agendamentos/{id}` - Atualiza os detalhes de um agendamento específico.
- `DELETE /agendamentos/{id}` - Exclui um agendamento específico.
- `GET /horarios/` - Retorna os horários disponíveis.
- `GET /prestadores/` - Lista todos os prestadores de serviços cadastrados.

## Permissões

- **IsPrestador:** Somente o prestador que criou o agendamento pode visualizar, editar ou excluir o agendamento.
- **IsOwnerOrCreateOnly:** Usuários podem criar agendamentos, mas só podem visualizar agendamentos se forem os prestadores associados.

## Tecnologias Utilizadas

- **Django:** Framework principal para desenvolvimento.
- **Django Rest Framework:** Para criação da API.
- **PostgreSQL:** Banco de dados relacional utilizado.
- **Docker:** Containerização para facilitar o desenvolvimento e a implantação.


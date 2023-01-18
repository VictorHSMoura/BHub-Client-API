# BHub-Client-API
API desenvolvida para a seleção de candidatos da empresa BHub.

## Requisitos

- [Python](https://www.python.org/downloads/) (versão utilizada 3.10)
- [Pip](https://pip.pypa.io/en/stable/installation/) (versão utilizada 22.3.1)

## Execução

### 1. Com Docker

Inicialmente, instale o [Docker](https://docs.docker.com/engine/install/ubuntu/) em seu computador. Após isso, execute no terminal:

```
  docker compose up
```

Após isso, a API estará disponível em `localhost:8000`.

### 2. Sem Docker

Antes de executar a API, é necessário conferir se o seu computador possui os requisitos necessários. Após isso, é necessário instalar os pacotes requeridos pelo projeto. Para isso, execute o comando abaixo na pasta raíz do projeto:

```
  pip install -r requirements.txt
```

Após instalar os pacotes, basta executar a API por meio do seguinte comando (também executado na pasta raíz do projeto):

```
  uvicorn app:app --reload
```

Com isso, o acesso a API podera ser feito por `localhost:8000`.

**OBS.:** Caso algum dos comandos não funcione, teste utilizar o prefixo `python3 -m ` antes do comando apresentado.

## Testes

Os testes dessa aplicação foram feitos utilizando a biblioteca pytest. Para executar os testes basta executar a seguinte linha na raíz do projeto:

```
  pytest
```
## Deploy

A API também está disponível na seguinte URL: https://bhub-api-victor-moura.herokuapp.com

# Teste para Desenvolvedor Júnior Python

## Descrição

O objetivo deste teste é avaliar sua habilidade em desenvolver uma API REST usando FastAPI, realizar o processamento de arquivos XML (Nota Fiscal Eletrônica - NFE), e persistir os dados em um banco.

### Funcionalidades

1. **Endpoint de Upload (POST /upload/)**
    - Permitir o upload de arquivos XML (NFE).
    - Realizar o processamento e extração dos dados relevantes do XML.
    - Validar o XML de entrada (certificar-se de que é uma NFE válida).

2. **Endpoints de Consulta Lista (GET /nfe/)**
    - Listagem de todas as NFes carregadas.

3. **Endpoints de Consulta ID(GET /nfe/{nfe_id})**
    - Exibição de detalhes específicos de uma NFE, buscada pelo seu ID ou chave de acesso.


## Pré-requisitos

* Python >= 3.8

## Instruções

Abra um terminal na pasta **Script** do projeto e execute o comando:
```
.\venv.bat
```
Abra outro terminal na pasta **Script** e execute  o comando:
```
.\start.bat
```
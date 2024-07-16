from fastapi import FastAPI, HTTPException, Query  # Importa classes e funções necessárias do FastAPI
import os, json  # Importa módulos do sistema operacional e para manipulação de JSON
import requests  # Importa a biblioteca requests para fazer solicitações HTTP
import shutil  # Importa a biblioteca shutil para operações de arquivos
import logging  # Importa a biblioteca de logging para registrar informações e erros
from datetime import datetime  # Importa datetime para manipular datas e horas
from pathlib import Path


from utils.find_links import find_links_at_level_one, find_links_at_level_two
from utils.scrapping import scrap_website

app = FastAPI()

# Configura o logging para registrar informações e erros
logging.basicConfig(level=logging.INFO)

@app.get("/")
def root():
    
    return {"message" : "Hello World!" }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Define uma rota GET para obter links do website
@app.get("/links/")
async def get_website_links():
    """
    Rota GET para obter links do primeiro nível de um website.

    Returns:
        dict: Um dicionário contendo uma lista de links encontrados.

    Raises:
        HTTPException: Se nenhum conteúdo ou link for encontrado.
    """

    website_content =  scrap_website("https://iseb3.com.br/respostas-em-planilhas")

    if not website_content:
        raise HTTPException(status_code=404,detail="Nenhum conteúdo encontrado")
    
    links = find_links_at_level_one(website_content)


    if not links:
        raise HTTPException(status_code=404,detail="Nenhum link encontrado")
    

    return {"links" : links}


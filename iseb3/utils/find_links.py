from fastapi import HTTPException
import logging
from bs4 import BeautifulSoup

def find_links_at_level_one(page_content: str):
    """
    Função para encontrar links no primeiro nível de uma página que atendam a critérios específicos.

    Args:
        page_content (str): O conteúdo HTML da página.

    Returns:
        list: Uma lista de URLs que atendem aos critérios de filtragem.

    Raises:
        HTTPException: Se ocorrer qualquer erro durante o processo de extração de links.
    """

    try:
        
        #Parsing do conteúdo HTML com BeatifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        #encontrando todos os links na página
        links = soup.find_all('a',href=True)

        filtered_links = []
        for link in links:
            href=link['href']
            logging.info(f"Link encontrado: {href}")
            if (href.startswith("http://iseb3.com.br/respostas-participantes") or
                href.startswith("http://iseb3.com.br/respostas-carteira") or
                "Respostas" in href):
                filtered_links.append(href)

        logging.info(f"Links Filtrados: {filtered_links}")
        return filtered_links
    except Exception as e:
        logging.error(f"Erro durante a extração de links:{e}")
        raise HTTPException(status_code=500,detail=str(e))
    

def find_links_at_level_two(page_contet: str) :
    """
        Função para encontrar links no segundo nível de uma página que contenham a string "Respostas".

        Args: 
            page_content(str): O conteúdo da página HTML.

        Returns: 
            list: Uma lista de URLs que contêm a string "Respostas".


        Raises:
            HTTPException: Se ocorrer qualquer erro durante o processo de extração de links.

    """

    try:
        soup = BeautifulSoup(page_contet,'html.parser')

        links = soup.find_all('a', href=True)
        filtered_links = []

        for link in links:
            href = link['href']
            logging.info(f"Link encontrado: {href}")
            if "Respostas" in href:
                filtered_links.append(href)

        logging.info(f"Links filtrados: {filtered_links}")
        return filtered_links
    except Exception as e:
        logging.error(f"Erro durante a extração de links: {e}")
        # Em caso de exceção, retorna detalhes do erro
        raise HTTPException(status_code=500, detail=str(e))
import requests
from bs4 import BeautifulSoup
from cria_audios import cria_audio



def ultimas_noticias():
    site = requests.get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for noticia in noticias.find_all('item')[:3]:
        msg = noticia.title.text
        print(msg)
        cria_audio(msg)
import json
import requests

from cria_audios import cria_audio

#####CONFIGURAÇÕES#####
APPID = 'ae31fa0afaad115481233cd0f1ab2c55'
CIDADE = 'goiânia'
PAIS = 'br'

def previsao_tempo(temp=False, minmax=False):
    site = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={CIDADE},{PAIS}&appid={APPID}&units=metric&lang=pt')
    clima = site.json()
    # print(json.dumps(clima, indent=4))
    descricao = clima['weather'][0]['description']
    tempo = clima['main']['temp']
    tempo_max = clima['main']['temp_max']
    tempo_min = clima['main']['temp_min']

    if temp:
        msg = f'No momento fazem {tempo} graus com {descricao}'

    if minmax:
        msg = f'Mínima de {tempo_min} e máxima de {tempo_max}'

    cria_audio('previsao_tempo',msg)

# previsao_tempo()
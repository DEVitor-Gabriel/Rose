import requests
import json

from cria_audios import cria_audio

def cotacao_moeda(moeda):
    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacoes_dic = cotacoes.json()
    # print(cotacoes_dic)

    dolar = cotacoes_dic['USD']['bid']
    euro = cotacoes_dic['EUR']['bid']
    bitcoin = cotacoes_dic['BTC']['bid']

    dolar = f'{float(dolar):_.2f}'
    euro = f'{float(euro):_.2f}'
    bitcoin = f'{float(bitcoin):_.3f}'

    if moeda == 'usd':
        dolar_list = dolar.split('.')
        msg = f'O valor do dólar hoje é {dolar_list[0]} R$ e {dolar_list[1]} Centavos'
        # print(msg)
        cria_audio('moeda', msg)
    
    if moeda == 'eur':
        euro_list = euro.split('.')
        msg = f'O valor do Euro hoje é {euro_list[0]} R$ e {euro_list[1]} Centavos'
        # print(msg)
        cria_audio('moeda', msg)

    if moeda == 'btc':
        btc_list = bitcoin.split('.')
        msg = f'O valor do Bitcoin hoje é {btc_list[0]} mil e {btc_list[1]} R$'
        # print(msg)
        cria_audio('moeda', msg)


    # print(dolar)
    # print(euro)
    # print(bitcoin)

# cotacao_moeda('usd')
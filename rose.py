import speech_recognition as sr
from playsound import playsound
import unidecode
#from subprocess import call #MAC / LINUX
from playsound import playsound
from comandos.cotacao_moedas import cotacao_moeda #WINDOWS

from comandos.noticias import ultimas_noticias
from comandos.playlists import playlist
from comandos.pontomais import pontomais
from comandos.previsao_tempo import previsao_tempo
from cria_audios import cria_audio
from datetime import datetime

hotword = 'rose'

def monitora_mic():

    mic = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            mic.adjust_for_ambient_noise(source)
            # mic.dynamic_energy_adjustment_ratio = 4
            print('Aguardando o Comando: ')
            audio = mic.listen(source)

            try:
                trigger = mic.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()
                # print(trigger)
                # trigger = unidecode.unidecode(trigger)
                if hotword in trigger:
                    print('Comando: ', trigger)
                    responde('espera ai')
                    executa_comando(trigger)
                    break
                    

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return trigger

def responde(arquivo):
    playsound(f'audios/{arquivo}.mp3')
    # toca_audio(arquivo)

def executa_comando(trigger):
    if 'notícias' in trigger:
        ultimas_noticias(hotword)

    elif 'toca' in trigger and 'costa gold' in trigger:
        playlist('costa_gold')

    elif 'tempo agora' in trigger or 'temperatura agora' in trigger:
        previsao_tempo(temp=True)
    
    elif 'temperatura' in trigger:
        previsao_tempo(minmax=True)

    elif 'dólar' in trigger:
        cotacao_moeda('usd')

    elif 'euro' in trigger:
        cotacao_moeda('eur')

    elif 'bitcoin' in trigger:
        cotacao_moeda('btc')

    elif 'bater o ponto' in trigger:
        hr_atual = datetime.now().time()
        hr_atual = str(hr_atual).split(':')

        if (12 <= int(hr_atual[0]) <= 14):
            pontomais()

        elif(17 <= int(hr_atual[0]) <= 19):
            pontomais()

        else:
            msg = 'Você não pode bater o ponto neste horário'
            cria_audio('pontomais_erro',msg)

    else:
        resposta = trigger.strip(hotword)
        cria_audio('resposta',resposta)
        print('Comando invalido')
        responde('comando_invalido')

def main():
    while True:
        monitora_mic()

main()
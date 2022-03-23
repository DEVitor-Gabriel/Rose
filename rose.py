import speech_recognition as sr
from playsound import playsound
import unidecode
#from subprocess import call #MAC / LINUX
from playsound import playsound #WINDOWS

from comandos.noticias import ultimas_noticias

hotword = 'ana'

def monitora_mic():

    mic = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print('Aguardando o Comando: ')
            audio = mic.listen(source)

            try:
                trigger = mic.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()
                trigger = unidecode.unidecode(trigger)
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
    if 'noticias' in trigger:
         ultimas_noticias()

def main():
    while True:
        monitora_mic()

main()
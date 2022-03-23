from gtts import gTTS
from toca_audio import toca_audio
import os


def cria_audio(nome,audio):
    path = f'audios/{nome}.mp3'

    tts = gTTS(audio, lang='pt-br')

    if os.path.exists(path):
        os.remove(path)

    tts.save(path)
    toca_audio(path)
    # Para reproduzir o audio
    
    # call(['afplay','audios/hello.mp3']) # OSX
    # call(['aplay','audios/hello.mp3'])  # Linux
    # playsound('audios/Mensagem Dinamica.mp3')# Windows

# cria_audio('invalido','Eu não sou obrigada a isso!')
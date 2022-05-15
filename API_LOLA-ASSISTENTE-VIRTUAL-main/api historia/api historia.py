import playsound
import speech_recognition as sr
import pyaudio
import pyttsx3
import unidecode

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')
        frase = unidecode.unidecode(frase)

        if 'bom' and 'dia' in frase.lower():
            engine.say('bom dia o que vamos fazer?')
            engine.runAndWait()
        elif 'boa' and 'tarde' in frase.lower():
            engine.say('Boa tarde o que vamos fazer?')
            engine.runAndWait()
        elif 'boa' and 'noite' in frase.lower():
            engine.say('boa noite o que vamos fazer?')
            engine.runAndWait()

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()

def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')
        frase = unidecode.unidecode(frase)

        if 'patinho' in frase.lower():
            playsound.playsound('patinho.mp3')

        elif 'chapeuzinho' in frase.lower():
            playsound.playsound('chapuzinho.mp3')

        elif 'porquinho' in frase.lower():
            playsound.playsound('porquinho.mp3')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()
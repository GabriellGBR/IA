import speech_recognition as sr
import unidecode


def abrir_mic():

    audio = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo")
        voz = audio.listen(source)
    try:
        comando = audio.recognize_google(voz, language="pt-BR")
        comando = comando.lower()
        comando = unidecode.unidecode(comando)
        print(comando)
    except:
        print("Não escutei")

def abrir_mic_2():

    audio = sr.Recognizer()
    with sr.Microphone() as source:
        voz = audio.listen(source)
    try:
        comando = audio.recognize_google(voz, language="pt-BR")
        comando = comando.lower()
        comando = unidecode.unidecode(comando)
        return comando
    except:
        print("Não escutei")



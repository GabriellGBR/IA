def abrir_mic():
    import speech_recognition as sr
    import unidecode

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
    return comando


def historia():
    import microfone
    import pyttsx3
    import playsound
    maquina = pyttsx3.init()
    voices = maquina.getProperty('voices')
    maquina.setProperty('voice', voices[-2].id)
    maquina.say('Oque vamos ouvir?')
    maquina.runAndWait()
    mic = microfone.abrir_mic()
    if 'patinho' in mic:
        playsound.playsound('patinho.mp3')
    if 'chapeuzinho' in mic:
        playsound.playsound('chapeuzinho.mp3')
    if 'porquinho' in mic:
        playsound.playsound('porquinho.mp3')

historia()



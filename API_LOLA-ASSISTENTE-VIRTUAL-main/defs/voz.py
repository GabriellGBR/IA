def maquina_voz(texto, printAtivo=True, runAndWait=True):
    import pyttsx3
    maquina = pyttsx3.init()
    voices = maquina.getProperty('voices')
    maquina.setProperty('voice', voices[-2].id)

    if printAtivo:
        print(texto)
    maquina.say(texto)
    if runAndWait:
        maquina.runAndWait()

def maquina_voz_en(texto, printAtivo=True, runAndWait=True):
    import pyttsx3
    maquina = pyttsx3.init()
    voices = maquina.getProperty('voices')
    maquina.setProperty('voice', voices[-1].id)

    if printAtivo:
        print(texto)
    maquina.say(texto)
    if runAndWait:
        maquina.runAndWait()
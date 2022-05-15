import microfone
import jogo
import historia
import pyttsx3


maquina = pyttsx3.init()
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[-2].id)

maquina.say('Ola, oque vamos fazer hoje? ')
maquina.runAndWait()
mic = microfone.abrir_mic()

if 'jogo' in mic:
    jogo.jogo()
if 'historia' in mic:
    historia.historia()

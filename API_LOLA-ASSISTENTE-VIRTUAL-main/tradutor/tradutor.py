from googletrans import Translator
from defs.microfone import abrir_mic_2
from defs.voz import *


def tradutor():
    maquina_voz("O que deseja traduzir?")
    print("Ouvindo")
    trad = Translator()
    traducao = trad.translate(abrir_mic_2(), dest="en")
    maq_trad = maquina_voz_en(traducao.text)
    return maq_trad

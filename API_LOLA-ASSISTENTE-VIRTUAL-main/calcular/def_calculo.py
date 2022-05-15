
def calculo():
    from microfone import abrir_mic
    from voz import maquina_voz
    comando = abrir_mic()


    if 'somar' in comando:

        maquina_voz('fale um numero para somar')
        num1 = int(abrir_mic())
        maquina_voz('fale outro numero para somar')
        num2 = int(abrir_mic())
        cont= (num1+num2)

        maquina_voz(f'{num1} mais {num2} é igual a {cont}')

    elif 'subtrair' in comando:

        maquina_voz('fale um numero para subtrair')
        num1 = int(abrir_mic())
        maquina_voz('fale outro numero para subtarir')
        num2 = int(abrir_mic())
        cont1= (num1-num2)
        cont2= (num2-num1)

        if num1>num2:
            maquina_voz(f'{num1} menos {num2} é igual a {cont1}')
        elif num2>num1:
            maquina_voz(f'{num2} menos {num1} é igual a {cont2}')
        

    elif 'multiplicação' in comando:

        maquina_voz('fale um numero para multiplicar')
        num1 = int(abrir_mic())
        maquina_voz('fale outro numero para multiplicar')
        num2 = int(abrir_mic())

        cont= (num1*num2)

        maquina_voz(f'{num1} vezes {num2} é igual a {cont}')

    elif 'dividir' in comando:

        maquina_voz('fale um numero divisor')
        num1 = int(abrir_mic())
        maquina_voz('fale outro numero dividento')
        num2 = int(abrir_mic())

        cont= (num1/num2)

        maquina_voz(f'{num1} dividido por {num2} é igual a {cont:.2f}')

calculo()
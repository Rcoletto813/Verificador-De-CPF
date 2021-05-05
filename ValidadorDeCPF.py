#numera o cpf
def NumerarCPF():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)

#verifica o tamanho do cpf
def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        #print(f"O CPF é invalido pois nele há {len(cpf)} caractres")
        return False
    else:
        return True

#verifica o primeiro digito do cpf
def primeiro_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        acumulador = 0 #acumula o resultado #5
        resultado = 0 #3
        controlador = 10 #1
        for numeros in cpf_numerado[0:9]: #2
            resultado = numeros * controlador #multiplica os valores
            acumulador += resultado
            controlador = controlador - 1 #diminui 1 do controlador
        acumulador= acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == cpf_numerado[9]:
            return True
        else:
            return False

#verifica o segundo digito do cpf
def segundo_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        acumulador2 = 0
        resultado2 = 0
        controlador2 = 11
        for numeros2 in cpf_numerado[0:10]:
            resultado2 = numeros2 * controlador2  # multiplica os valores
            acumulador2 += resultado2
            controlador2 = controlador2 - 1  # diminui 1 do controlador
        acumulador2 = acumulador2 * 10 % 11
        if acumulador2 == 10:
            acumulador2 = 0
        if acumulador2 == cpf_numerado[10]:
            return True
        else:
            return False


cpf_numerado = []
cpf = str(input("Qual o seu CPF? Com ou sem pontuacao ")).replace('.', '').replace('-', '')#recebe o cpf da pessoa

NumerarCPF()
#print(cpf_numerado)
quantidade()

primeiro_digito()

segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("O CPF é valido")
else:
    print("O CPF é invalido")
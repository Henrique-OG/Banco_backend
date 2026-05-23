
def validar_numero_inteiro(numero):
    numero = str(numero)
    while numero.isnumeric() == False:
        print('NUMERO INVALIDO')
        numero = input('Digite um valor valido: ')
    return int(numero)

def validar_escolha(escolha, quantidade):
    while escolha not in range(1, quantidade + 1):
        print('Opção invalida')
        escolha = validar_numero_inteiro(input('Digite um valor valido: '))
    return escolha

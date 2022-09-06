#A logica deste programa foi finalizada no dia: 05/09/2022 as 22:05 da noite.
#Programa feito por github@vinicius-goncalves.

opcao_escolhida = None

def invocar_menu():
    print('''
    Calculo de IMC 
    Accesse as opções abaixo de acordo com o número
        1. Calculo IMC
        2. Creditos
        3. Sair
    ''')

def invocar_while():

    opcao = input('Escolha a opcao: ')
    opcao = int(opcao)
    global opcao_escolhida
    opcao_escolhida = opcao

    while opcao > 3 or opcao <= 0:
        print(f'Opcao invalida')
        invocar_menu()
        opcao = input('Escola a opcao: ')
        opcao_escolhida = opcao

invocar_menu()
invocar_while()

def imprimir_informacao(peso, altura, imc, classificacao):
        print(f'''
    Peso: {peso}kg
    Altura: {altura}m
    IMC: {imc:2.2f}kg/m2
    Classificação: {classificacao}
    ''')

def iniciar_consulta():
    
        peso = input('Insira o peso da pessoa: ')
        altura = input('Insira a altura da pessoa: ')

        peso = float(peso)
        altura = float(altura)

        imc = peso / (altura * altura)
        if imc <= 18.5:
            imprimir_informacao(peso, altura, imc, 'Abaixo do peso normal')
        elif imc >= 18.6 and imc <= 24.9:
            imprimir_informacao(peso, altura, imc, 'Peso normal')
        elif imc >= 25 and imc < 29.99:
            imprimir_informacao(peso, altura, imc, 'Excesso de peso')
        elif imc >= 30 and imc <= 34.9:
            imprimir_informacao(peso, altura, imc, 'Obsedidade classe I')
        elif imc >= 35 and imc <= 39.9:
            imprimir_informacao(peso, altura, imc, 'Obesidade classe II')
        elif imc >= 40:
            imprimir_informacao(peso, altura, imc, 'Obesidade classe III')
        
        continuar = input('Realizar outra consulta? Escreva "S" para sim, e "N" para nao: ')
        if continuar == 'S':
            iniciar_consulta()
        else:
            print('Saindo do programa.')

if(opcao_escolhida == 1):
    iniciar_consulta()
if(opcao_escolhida == 2):
    print('''
Programa criado por: Vinicius Goncalves
Project source on Github: https://github.com/vinicius-goncalves/python-imc-calculator
    ''')

    invocar_menu()
    invocar_while()

if(opcao_escolhida == 3):
    print('Saindo do programa.')
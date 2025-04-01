# Calculadora em Python Versão 2.0
def bem_vindo(): # Definindo Função de Boas Vindas
    print('''
\n******** Calculadora Python Versão 2.0*******
''')


def calculadora(): # Função de Calculadora
    # Apresentando as opções para o usuário
    escolha = input('''
Selecione a operação desejada: \n
1 -> Soma
2 -> Subtração
3 -> Multiplicação
4 -> Divisão \n
''')

    num1 = int(input('\nDigite o primeiro número: ')) 
    num2 = int(input('\nDigite o segundo número: ')) 

# Estrutura de Condicional da calculadora
# Observe que não definimos uma função para cada operação. Fazemos o cálculo conforme a escolha da opção e imprimimos o resultado na tela. Tudo dentro da condicional.
    if escolha == '1':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif escolha == '2':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif escolha == '3':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif escolha == '4':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)
    else:
        print("\nOpção Inválida!")

    retorno() # Chama a função que criamos abaixo para que o usuário passa escolher continuar ou não no programa
#OBSERVAÇÃO: é importante destacar que sogo após a linha "def calculadora ():" até este comentário, faz tudo parte da função "calculadora". Observe a identação do código. 
	

# Criamos aqui uma função para perguntar ao usuário se ele quer continuar a utilizar a calculadora ou não
def retorno():
    calc_retorno = input('''
Você deseja utilizar a calculadora novamente?\n
Caso sim, digite "S". Caso não, digite "N"
''')

    if calc_retorno.upper() == 'S':
        calculadora()
    elif calc_retorno.upper() == 'N':
        print('Até Logo!!!')
    else:
        retorno()

bem_vindo() # Iniciando nossa calculadora com a mensagem de boas vindas
calculadora() # Após mensagem de boas vindas, chamamos a calculadora

"""
Treinar é parte do aprendizado. Não queremos que você apenas execute o código, mas que entenda, que realize testes.
Faça alterações, proponha melhorias.
Insira por exemplo, a função de potência.
Tente controlar a escolha do usuário antes de dar a opção de digitar os números. faça que, caso a opção escolhida seja diferente de 1 a 4, a informação de opção inválida seja exibida antes de que o usuário digites os números para execução da operação.
"""
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome=input('Digite seu nome:')
idade=input('Digite sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é ', nome[::-1])
    if(f' ' in nome):
        print('Seu nome contém espaços')
        print('Seu nome tem ',len(nome), 'letras')
    else:
            print('Seu nome não contém espaços')
            print('Seu nome contém', len(nome), ' letras')
   
    print('A última letra do seu nome é ', nome[-1])
else:
    print('Campos vazios')
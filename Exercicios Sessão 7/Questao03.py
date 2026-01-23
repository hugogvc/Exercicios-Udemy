"""
. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""


def maior():
    
    cont = int(input("Quantos numeros voce quer na sua lista: "))
    lista = []
    
    
    for i in range(cont):
        while cont > 0:
            
            num = int(input(f"Digite o {1 + i} numero: "))
            lista.append(num)
            cont = cont-1
            i = i + 1
      
    maior_valor = max(lista)
       
    print(f"O maior numero da sua lista é {maior_valor}")
    return maior_valor
    
maior()
    

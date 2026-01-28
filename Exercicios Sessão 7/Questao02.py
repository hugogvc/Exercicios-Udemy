"""
Escrever as datas por extenso

"""


def extenso(data: str) -> None:

   # data = input("Digite a data no formato dd/mm/aaaa: ")

    dia, mes, ano = data.split("/")

    # Escrevendo mês
 
    nome_mes = {
    "01" : "Janeiro",
    "02" : "Fevereiro",
    "03" : "Março",
    "04" : "Abril",
    "05" : "Maio",
    "06" : "Junho",
    "07" : "Julho",
    "08" : "Agosto",
    "09" : "Setembro",
    "10" : "Outubro",
    "11" : "Novembro",
    "12" : "Dezembro"
    }

    if mes in nome_mes:
        resultado = f"{dia} de {nome_mes.get(mes)} de {ano}"
        print(resultado)
    else:
        resultado = ("Formato invalido")
        print(resultado)
    
    return resultado  

if __name__ == '__main__':
    extenso('01/01/2024')

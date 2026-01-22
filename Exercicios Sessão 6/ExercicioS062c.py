# 2 c)




A = []

for i in range(10):
    valor = int(input(f"Informe o {i+1} valor: "))
    A.append(valor)
    
for i in range(len(A)):
    if A[i] % 2 == 0:
        print(f"{A[i]} é um número par")

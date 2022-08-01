listNum = []
maior = menor = 0
for iten in range(2):
    listNum.append(int(input(f'Escreva um número na posição {iten +1}: ')))
    if iten == 0:
        maior = menor = listNum[iten]
    else:
        if listNum[iten] > maior:
            maior = listNum[iten]
        if listNum [iten] < menor:
            menor = listNum[iten]

#listNum.sort() #---> O comando sort() coloca uma lista em ordem crescente ou decrecente --> (reverse=True)
print(f' Você digitou os seguintes números {listNum}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'A diferença entre eles é: {maior - menor}')
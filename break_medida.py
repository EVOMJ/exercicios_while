soma =0
nota =0
nome = input("digite o nome do aluno :")

while True:
    nota = float (input ('digite a nota do aluno: \n ou \n digite a 99 para SAIR :'))
    if nota == 99:
         break
    soma += nota 
print(f' A média do aluno {nome}  é  {soma / 4} 😎👍')

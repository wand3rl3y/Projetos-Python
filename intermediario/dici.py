dicinario1 = {'chave1': 'valor da chave1'} # chaves tem que ser unicas
d2 = { 1: 'valor1', 2: 'valor2' , 3:'valor3'}

print(dicinario1)
print(dicinario1['chave1']) # acessando o valor da chave
print(d2)

dici2 = d2

dici2[1] = 'novo valor da chave'

print(d2)
print(dici2) # em um dici para criar uma copa igual temos que usar outro metodo deepcopy
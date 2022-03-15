a = lambda x, y: x * y 

print(a(2,2))

lista = [
    ['P1' , 12],
    ['P2' , 2],
    ['P3' , 1],
]
#lista.sort() # não muda nada pois soa duas lista uma dentro da outra 
#mudando com funcao lambda , sort muda a lista
lista.sort(key=lambda item: item[1])
print(lista)
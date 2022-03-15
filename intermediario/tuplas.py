# Elementos de uma tupla não sao editaveis como lista 

tupla1 = (1,2,3, 'a', 'wanderley')

print(type(tupla1))
print(tupla1)

#para ser modificado tranforma uma tupla em lista

tupla1 = list(tupla1)
print(type(tupla1))
print(tupla1)
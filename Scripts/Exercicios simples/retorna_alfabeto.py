# Implemente uma função que receba uma string
# e retorne o conjunto das letras que ela contém, ou
# seja, o alfabeto que a produziu. Dica: Elimine o
# espaço após gerar o conjunto.

def getAlfabeto(sentenca):
    l = [i.upper() for i in sentenca]
    c = set(l)
    c.remove(' ')
    return c
        

s = input('Digite uma sentença: \n')
print(getAlfabeto(s))

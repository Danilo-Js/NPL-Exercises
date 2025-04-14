# Faz calculos de relevancias de expresões, em 9 romances de Machado de Assis

from nltk.corpus import machado
import math

colecao = []

# CALCULO RELEVANCIA DE EXPRESSOES
def tf(termo, doc):
    frequenciaTermo = colecao[doc].count(termo)
    termosNoDocumento = len(colecao[doc])   
    return frequenciaTermo/termosNoDocumento

def df(termo):
    frequencia = 0
    for i in colecao:
        if (i.count(termo) > 0):
            frequencia += 1
    return frequencia

def idf(termo):
    return (math.log10(len(colecao)/df(termo)))

def tfidf(termo,doc):
    return(tf(termo,doc)*idf(termo))

# PREENCHE A COLECAO 
def limpar(lista):
    lixo='.,:;?!"\'()[]{}\/|#$%^&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' in x]

for i in range(1,10):
    texto = machado.raw('romance/marm0'+str(i)+'.txt')
    textoLimpo = limpar(texto.split())
    colecao.append(textoLimpo)

# TESTE
termo = 'capitu'
print("df: " + str(df(termo)))
print("idf: " + str(idf(termo)))



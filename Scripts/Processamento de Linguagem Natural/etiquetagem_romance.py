# Script simples de etiquetagem

from nltk.corpus import machado
import spacy

texto = machado.raw('romance/marm01.txt')

palavras = texto.split()
palavras_distintas = set(palavras)

print(len(palavras))
print(len(palavras_distintas))

print(machado.fileids())

nlp = spacy.load('pt_core_news_sm')
doc = nlp('Será que vai funcionar essa etiquetagem?')
etiq = [(x.orth, x.pos) for x in doc]
print(etiq)
#!/usr/bin/python

import re
from collections import defaultdict
from collections import Counter

########## FUNÇÔES ############

#Lê um arquivo e retorna o seu conteúdo
def ler(nome_arq):
	arquivo = open(nome_arq, 'r', encoding='utf-8')
	conteudo_arq = arquivo.read()
	arquivo.close()
	return conteudo_arq

#Recebe uma lista de palavras e limpa pontuações, converte para minúsculas e deixa apenas palavras e palavras com hifen
def limpar(lista):
	lixo='.,:;?!"\'()[]{}\/|#$%^&*'
	quase_limpo = [x.strip(lixo).lower() for x in lista]
	return [x for x in quase_limpo if x.isalpha() or '-' in x]

########## PROGRAMA ############

########## PREPARAÇÃO DO CORPUS #################

# Leitura do corpus completo
corpus_base = ler('corpus_bruto.txt')	

# Divisão em sentenças
corpus_pontuacao = re.sub(r'\!|\?|\.', '#', corpus_base)
sents = corpus_pontuacao.split('#')
sents.remove('\n')

# Limpeza das sentenças e inclusão dos marcadores de início (<s>) e fim (</s>)
sentencas = [ ['<s>'] + limpar(s.split()) + ['</s>'] for s in sents ]

#print(sentencas)

# Gravação do corpus preparado
arquivo = open('corpus_preparado.txt', 'w', encoding='utf-8')
for s in sentencas:
	sentenca = ' '.join(s)
	arquivo.write(sentenca + '\n')
arquivo.close()

######### CRIAÇÃO DE UM CORPUS DE TREINO E TESTE ######################

# Leitura do corpus preparado
arquivo = open('corpus_preparado.txt', 'r', encoding='utf-8')
sentencas = arquivo.readlines()
arquivo.close()

corte = int(len(sentencas) * 0.8)               # Usa-se int para retornar o valor inteiro correspondente.
treino = sentencas[:corte]
teste = sentencas[corte:]

arquivo = open('corpus_treino.txt', 'w', encoding='utf-8')
for s in treino:
	arquivo.write(s)
arquivo.close()

arquivo = open('corpus_teste.txt', 'w', encoding='utf-8')
for s in teste:
	arquivo.write(s)
arquivo.close()

######### CONSTRUÇÃO DO MODELO ######################

arquivo = open('corpus_treino.txt', 'r', encoding='utf-8')
sentencas = arquivo.readlines()
arquivo.close()

'''
# Extração do vocabulário e contagem de ocorrências
vocab = set()
contagem = defaultdict(int)
for linha in sentencas:
	sent = linha.split()
	for palavra in sent:
		vocab |= {palavra}
		contagem[palavra] += 1


# Opção: Extração do vocabulário e contagem de ocorrências
contagem = defaultdict(int)
for linha in sentencas:
	sent = linha.split()
	for palavra in sent:
		contagem[palavra] += 1

vocab = set(contagem.keys())
'''
# Opção: Extração do vocabulário e contagem de ocorrências
palavras = list()
for linha in sentencas:
	palavras += linha.split()
contagem = Counter(palavras)	
vocab = set(contagem.keys())

'''
print(vocab)
print(len(vocab))
for (p, c) in contagem.items():
	print(p, '\t', c)
'''

# Filtragem e substituição de hápax legômena
hapax = [p for p in contagem.keys() if contagem[p] == 1]
novo_vocab = vocab - set(hapax)
novo_vocab |= {'<DES>'}

# Contagem de unigramas e bigramas
def ngramas(n, sent):
	return[tuple(sent[i:i+n]) for i in range(len(sent) - n + 1)]

#lista_str = 'parabéns pra você nesta data querida'.split()
#bigramas = ngramas(2,lista_str)
#print(bigramas)

# Criação dos dicionários de unigramas e bigramas
unigramas = defaultdict(int)
bigramas = defaultdict(int)

# Substitui os hápax no corpus de treino e acrescenta os unigramas e bigramas com suas contagens nos dicionários correspondentes
for linha in sentencas:
	sent = linha.split()

	for i in range(len(sent)):
		if sent[i] in hapax:
			sent[i] = '<DES>'

	uni = ngramas(1,sent)
	bi = ngramas(2,sent)

	for x in uni:
		unigramas[x] += 1
	
	for x in bi:
		bigramas[x] += 1

# Retorna probabilidade de um unigrama com suavização de Laplace

#for (p, c) in unigramas.items():
#	print(p, '\t', c)

#for (p, c) in bigramas.items():
#	print(p, '\t', c)

def prob_uni(x):
	C = sum(unigramas.values())
	V = len(novo_vocab)
	return (unigramas[x] + 1) / (C + V) 

# Retorna probabilidade de um bigrama com suavização de Laplace
def prob_bi(x):
	V = len(novo_vocab)
	return (bigramas[x] + 1) / (unigramas[(x[0],)] + V) 

#print(prob_uni(('o',)))
#print(prob_bi(('<s>','o')))

############# PREVISOR DE PALAVRAS ##############################
def prever(palavra):
	lista = [ch for ch in bigramas.keys() if ch[0] == palavra]
	ordem = sorted(lista, key=lambda x:prob_bi(x), reverse=True)
	topo = ordem[0][1]
	return topo

print(prever('brigou'))




			
	






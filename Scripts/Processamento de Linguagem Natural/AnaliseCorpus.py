#!/usr/bin/python

import nltk
from collections import defaultdict

########## FUNÇÔES ############

#Lê um arquivo e retorna o seu conteúdo
def ler(nome_arq):
	arquivo = open(nome_arq, 'r', encoding='utf-8')
	conteudo_arq = arquivo.read()
	arquivo.close()
	return conteudo_arq

#Busca expressões alvo em um texto e retorna seu contexto a direita e a esquerda em 80 caracteres
def concordanciador(alvo, texto):
	texto = texto.replace('\n', ' ')
	texto = texto.replace('\t', ' ')
	ocorrencias = list()
	encontrado_aqui = texto.find(alvo,0)
	while encontrado_aqui > 0:
		pos_inicial = encontrado_aqui - (40 - len(alvo) // 2)
		ocorrencias.append(texto[pos_inicial:pos_inicial+80])
		encontrado_aqui = texto.find(alvo, encontrado_aqui+1)
	return ocorrencias

#Limpa pontuações, converte para minúsculas e deixa apenas palavras e palavras com hifen
def limpar(lista):
	lixo='.,:;?!"\'()[]{}\/|#$%^&*'
	quase_limpo = [x.strip(lixo).lower() for x in lista]
	return [x for x in quase_limpo if x.isalpha() or '-' in x]

# Retorna um dicionário com as palavras e o número de ocorrências das palavras
def ocorrencias(lista_palavras):
	dicionario = defaultdict(int)
	for p in lista_palavras:
		dicionario[p] += 1
	return dicionario
	


########## PROGRAMA ############

texto = ler('Ubirajara.txt')
#print(texto)

#Percorre por linhas
#arquivo = open('Ubirajara.txt', 'r', encoding='utf-8')
#for linha in arquivo:				#Leitura de linhas a partir da referência pro arquivo
#	print(linha)

#for linha in arquivo.readlines():		#Leitura de linhas a partir do método readlines(). Para ler uma por vez, use readline()
#	print(linha)

#print(arquivo.read(20))

#saida = open('Novo.txt', 'w')			#Abre novo arquivo para escrita
#saida.write("Oi menina!")			#Escreve "Oi menina" no arquivo
#arquivo.close()


print("Número de caracteres: ", len(texto))	#Retorna qtde de caracteres no texto pq o texto é uma string que contém todo o livro

resultados = concordanciador('serpente', texto)
for i in resultados:
	print(i)

print("Número de ocorrências da palavra serpente: ", len(resultados))

palavras = texto.split()
palavras_sel = limpar(palavras)
print('Número de palavras antes da limpeza: ', len(palavras))
print('Número de palavras após a limpeza: ', len(palavras_sel))

vocabulario = set(palavras)
print('O vocabulário do corpus é composto por: ', len(vocabulario), ' palavras')

riqueza = len(vocabulario)/len(palavras)
print('A riqueza do vocabulário é: ', riqueza)

# Imprime chave valor do dicionário sem nenhuma ordenação
#dic = ocorrencias(palavras)
#for chave, valor in dic.items():	# O método items() em um dicionário gera uma sequencia de tuplas chave/valor
#	print(chave, '\t', valor) 

dic = ocorrencias(palavras)
mf = sorted(dic.items(), key = lambda tupla:tupla[1], reverse=True)[:50]
for chave, valor in mf:				# O método items() em um dicionário gera uma sequencia de tuplas chave/valor
	print(chave, '\t', valor) 


vazias = nltk.corpus.stopwords.words('portuguese')	#obtém stopwords pro português
frequentes_plenas = [chave for chave, valor in mf if chave.lower() not in vazias]
print("Frequentes que não são stopwords: ", frequentes_plenas)

#hapax = [x for x in palavras if palavras.count(x) == 1]
#hapax = [chave for chave, valor in dic.items() if valor == 1]
#print(hapax)

stemmer = nltk.stem.RSLPStemmer()
raizes = [stemmer.stem(x) for x in set(palavras)]
hapax_stem = [x for x in raizes if raizes.count(x) == 1]
print(hapax_stem)

print("Riqueza lexical: ", len(set(raizes))/len(raizes))

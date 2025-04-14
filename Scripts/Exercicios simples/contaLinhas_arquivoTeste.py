# Conta as linhas do arquivo teste

arq = open('arquivoTeste.txt', 'r')
lines = arq.read()
arq.close()
print(len(lines))

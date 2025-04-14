# 1) Calcular o uso médio de uma classe de
# palavras (advérbios) em diferentes tipos literários da
# produção machadiana (romances e crônicas).

# 2) Para cada obra:
# – Obter a string associada à obra usando o método raw()
# – Etiquetar o texto
# – Obter a lista de advérbios do texto
# – Armazenar a proporção de advérbios para o total de etiquetas

# 3) Gerar as estatísticas (média e desvio-padrão) para cada conjunto de
# dados (romances e crônicas)

from nltk.corpus import machado
import statistics as stat
import matplotlib.pyplot as plt
import spacy
nlp = spacy.load('pt_core_news_sm')

### CRONICAS
lista_cronicas = []
for i in range(1,6):
  lista_cronicas.append('cronica/macr0'+str(i)+'.txt')

prop_cronicas = []
for i in lista_cronicas:
    texto = machado.raw(i)
    doc = nlp(texto)
    etiq = [(x.orth_, x.pos_) for x in doc]
    lista_adv = [(pal,pos) for (pal,pos) in etiq if pos == 'ADV']
    prop_cronicas.append(len(lista_adv)/len(etiq))

cron_m = stat.mean(prop_cronicas)
cron_dp = stat.stdev(prop_cronicas)

### ROMANCES
lista_romances = []
for i in range(1,6):
  lista_romances.append('romance/marm0'+str(i)+'.txt')

prop_romances = []
for i in lista_romances:
    texto = machado.raw(i)
    doc = nlp(texto)
    etiq = [(x.orth_, x.pos_) for x in doc]
    lista_adv = [(pal,pos) for (pal,pos) in etiq if pos == 'ADV']
    prop_romances.append(len(lista_adv)/len(etiq))


rom_m = stat.mean(prop_romances)
rom_dp = stat.stdev(prop_romances)

### GRAFICO DE BARRAS
tipo_obra = ['Romances', 'Crônicas']
x = [0,1]
y = [rom_m, cron_m]
dp = [rom_dp, cron_dp]
plt.bar(x,y, yerr = dp)
plt.xticks(x, tipo_obra)
plt.ylabel('Percentual médio dos advérbios (%)')
plt.title('Adverbiação média em obras de M. de Assis')
plt.show()

import statistics

lista = list()

for i in range(3):
    lista.append(float(input("Intrduzca numero: ")))

med = statistics.fmean(lista)
medi = statistics.median(lista)
var = statistics.variance(lista)

print("Lista: ", lista)
print("Media:", med,  " Mediana:",medi,  " Varianza:", var)
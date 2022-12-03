import os
import csv
import statistics

file = os.path.join('data.csv')  # ruta del archivo
values = ''
# numero total de lineas
with open(file) as f:
    total_lines = sum(1 for line in f)
    print('Total lines: '+str(total_lines))

with open(file) as f:
    for row in f:
        values += row
# imprime las cadenas
with open(file, newline='') as f:
    spamreader = csv.reader(f, delimiter=',')
    for row in spamreader:
        print(','.join(row))

values = values.split('\n')
values_total = len(values)
for i in range(values_total):
    # quita la fecha de la cadena
    value = values[i]
    value = value[11:]  # elimino la fecha
    value = value.split(',')
    # convierte a enteros una lista de datos numerica
    values_int = list(map(int, value))
    print(values_int)
    total = sum(values_int)
    maxim = max(values_int)
    minimum = min(values_int)
    average = statistics.mean(values_int)
    print('Total: '+str(total)+', Value Max: : '+str(maxim)+' , Value Minim: ' +
          str(minimum)+', Average: '+str(average))
    i += 1

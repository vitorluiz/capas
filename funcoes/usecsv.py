import csv

with open('/home/vitorluiz/Documentos/capas/csv/mtc.csv', encoding='UTF-8', errors='ignore') as file:
    _csv = csv.reader(file, delimiter=';')
    _csv.__next__()
    for x in _csv:
        print(f"{x[0]}-{x[1]}-{x[2]}-{x[6]}")

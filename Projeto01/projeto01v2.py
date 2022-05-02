import json
from pickle import APPEND
from turtle import clear
import bibtexparser
import csv
import pandas as pd
import yaml

bib_data = []
ordenado = []
colunas = []
aux_list= []
arquivos = ['ScienceDirect_citations_Todos.bib','iee02.bib','acm_all.bib']


## funcao criada para abrir os arquivos e retornar os registros de referencias
def abrir_arqs(nomeArq):
    with open(nomeArq, 'r', encoding="utf8") as bibtex_file:
        bib_dados = bibtexparser.load(bibtex_file)
    return(bib_dados.entries)

for arquivo in arquivos:
    ## bib_data aglomera os registros de todos os arquivos
    bib_data.extend(abrir_arqs(arquivo))

## percorre o dict bib_data
for i in range(len(bib_data)):
    ## troca chave ENTRYTYPE por type_publication para padronização
    bib_data[i]['type_publication'] = bib_data[i]['ENTRYTYPE']
    del bib_data[i]['ENTRYTYPE']
    
    ## preenche a variavel coluna com todas as chaves para montagem do csv
    for titulo in bib_data[i].keys():
        if titulo not in colunas:
            colunas.append(titulo)

## ajusta colunas e campos para preenchimento do csv
for i in range(len(bib_data)):
    aux_list.clear()
    for x in colunas:
        if x in bib_data[i].keys():
            aux_list.append(bib_data[i][x])
        else:
            aux_list.append('')
    ordenado.append(dict(zip(colunas, aux_list)))

## Cria arquivo CSV
with open('csvreferencias7.csv', 'w', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=colunas)
    writer.writeheader()
    writer.writerows(ordenado)

## Cria arquivo JSON
with open('referencias12.json','w') as f_jason:
    json.dump(bib_data, f_jason)

## Cria arquivo Yaml
with open('referencias2.yaml','w') as f_yaml:
    yaml.dump(bib_data, f_yaml)
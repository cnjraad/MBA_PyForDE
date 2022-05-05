import json
from pickle import APPEND
from turtle import clear
import bibtexparser
import csv
import pandas as pd
import yaml as yml

formatFile = []
bib_data = []
ordenado = []
colunas = []
aux_list = []
arquivos = ['ScienceDirect_citations_Todos.bib', 'iee02.bib', 'acm_all.bib']

# CARREGA O ARQUIVO DE CONFIGURAÇÃO
dirConfig = r'C:\Users\mclst\OneDrive\Documentos\Projeto_2\Config'
configFile = 'config.yml'

with open(dirConfig + '\\' + configFile) as f:
    configFile = yml.load(f, Loader=yml.loader.SafeLoader)

# funcao criada para abrir os arquivos e retornar os registros de referencias


def abrir_arqs(nomeArq):
    with open(nomeArq, 'r', encoding="utf8") as bibtex_file:
        bib_dados = bibtexparser.load(bibtex_file)
    return(bib_dados.entries)


for arquivo in arquivos:
    # bib_data aglomera os registros de todos os arquivos
    bib_data.extend(abrir_arqs(arquivo))

# percorre o dict bib_data
for i in range(len(bib_data)):
    # troca chave ENTRYTYPE por type_publication para padronização
    bib_data[i]['type_publication'] = bib_data[i]['ENTRYTYPE']
    del bib_data[i]['ENTRYTYPE']

    # preenche a variavel coluna com todas as chaves para montagem do csv
    for titulo in bib_data[i].keys():
        if titulo not in colunas:
            colunas.append(titulo)

# ajusta colunas e campos para preenchimento do csv
for i in range(len(bib_data)):
    aux_list.clear()
    for x in colunas:
        if x in bib_data[i].keys():
            aux_list.append(bib_data[i][x])
        else:
            aux_list.append('')
    ordenado.append(dict(zip(colunas, aux_list)))


# Criar arquivos


def funCriarArquivos(formato):

    formatFile = formato

 # Cria arquivo CSV
    if formatFile == 'CSV':
        with open('csvreferencias7.csv', 'w', encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=colunas)
            writer.writeheader()
            writer.writerows(ordenado)

 # Cria arquivo JSON
    elif formatFile == 'JSON':
        with open('referencias12.json', 'w') as f_jason:
            json.dump(bib_data, f_jason)

 # Cria arquivo Yaml
    elif formatFile == 'YAML':
        with open('referencias2.yaml', 'w') as f_yaml:
            yml.dump(bib_data, f_yaml)
    else:
        print('Formato não disponivel.')


# Switch escolha opções de arquivos
print('Escolha uma opção de arquivo')
print('1 - CSV')
print('2 - JSON')
print('3 - YML')
print('4 - Todos')
entrada = input('Insira o numero da opção desejada: ')

if entrada == '1':
    formato = 'FILECSV'
    funCriarArquivos(
        configFile['FILECSV']
    )
elif entrada == '2':
    formato = 'FILEJSON'
    funCriarArquivos(
        configFile['FILEJSON']
    )
elif entrada == '3':
    formato = 'FILEYML'
    funCriarArquivos(
        configFile['FILEYML']
    )
elif entrada == '4':

    formato = 'FILECSV'
    funCriarArquivos(
        configFile['FILECSV']
    )
    formato = 'FILEJSON'
    funCriarArquivos(
        configFile['FILEJSON']
    )
    formato = 'FILEYML'
    funCriarArquivos(
        configFile['FILEYML']
    )

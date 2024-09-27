import csv
import os

pessoas = []
pessoa = {}
file_exists = os.path.isfile('pessoas.csv')

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['telefone'] = input('Telefone: ')
    pessoas.append(pessoa.copy())
    if input('Deseja inserir mais uma pessoa? [s/n]: ').lower() not in ('s', 'sim'):
        break

with open('pessoas.csv', mode='a', newline='', encoding='utf-8') as file:
    fieldnames = ['nome', 'idade', 'telefone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    for pessoa in pessoas:
        writer.writerow(pessoa)
print('--- Usando for ---')
for pessoa in pessoas:
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos e o seu telefone é {pessoa['telefone']}")

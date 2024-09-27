import csv
import os

Funcionarios = []
funcionario = {}
file_exists = os.path.isfile('Funcionarios.csv')

while True:
    funcionario['id'] = str(input('id: '))
    funcionario['nome'] = input('nome: ')
    funcionario['horas'] = int(input('horas: '))
    funcionario['custo'] = int(input('custo: '))
    Funcionarios.append(funcionario.copy())
    if input('Deseja inserir mais uma pessoa? [s/n]: ').lower() not in ('s', 'sim'):
        break

with open('Funcionarios.csv', mode='a', newline='', encoding='utf-8') as file:
    fieldnames = ['id', 'nome', 'horas', 'custo']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    for funcionario in Funcionarios:
        writer.writerow(funcionario)
print()
for funcionario in Funcionarios:
    print(f"O funcionario {funcionario['id']} cujo nome é {funcionario['nome']} cumpriu {funcionario['horas']} e ganhou {funcionario['custo']} doletas")
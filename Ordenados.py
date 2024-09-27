import csv
import os

salarios = []

with open("Funcionarios.csv", mode='r') as csv_file:
    csvreader = csv.reader(csv_file)
    header = next(csvreader)
    funcionarios = []



    for funcionario in csvreader:
        funcionarios.append(funcionario)


    for funcionario in funcionarios:

        id_funcionario = funcionario[0]
        salario_total = int(funcionario[2]) * int(funcionario[3])
        salarios.append({'id': id_funcionario, 'total': salario_total})

    file_exists = os.path.isfile('Funcionarios.csv')

    with open('Funcionarios.csv', mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['id' 'nome', 'horas', 'custo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only if the file is new

        for funcionario in funcionarios:
            writer.writerow(funcionario)




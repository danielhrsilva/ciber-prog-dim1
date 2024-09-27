#CSV - Comma separated Values
#RFC 4180 - Permite criar CSV



pessoas = []
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['telefone'] = input('Telefone: ')
    pessoas.append(pessoa.copy())
    if input('Deseja inserir mais uma pessoa? ') not in ('s', 'sim'):
        break

for pessoa in pessoas:
    print(f'Nome:{pessoa["nome"]} idade:{pessoa['idade']} telefone:{pessoa["telefone"]}')
    print()

for x in range(len(pessoas)):
    print(f'Nome:{pessoa["nome"]} idade:{pessoa['idade']} telefone:{pessoa["telefone"]}')
    print()

x = 0
while x < len(pessoas):
    print(f'Nome:{pessoa["nome"]} idade:{pessoa['idade']} telefone:{pessoa["telefone"]}')
    print()
    x += 1
vendas = [
   [
       [10, 20, 30, 40],
       [50, 60, 70, 80],
   ],
   [
       [90, 100, 110, 120],
       [130, 140, 150, 160]
   ],
   [
       [170, 180, 190, 200],
       [210, 220, 230, 240]
   ]
]


total = 0
for profundidade in range(3):
   total_profundidade = 0
   for coluna in range(4):
       total_linha = 0
       for linha in range(2):
           total = total + vendas[profundidade][linha][coluna]
           total_linha = total_linha + vendas[profundidade][linha][coluna]
       print(f'Total da linha {linha}: {total_linha}')
       total_profundidade = total_profundidade + total_linha
   print(f'Total da profundidade {profundidade}: {total_profundidade}')
print(f'Total de vendas: {total}')
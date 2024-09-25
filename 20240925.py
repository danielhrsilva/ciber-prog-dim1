vendas = 0
total = 0
xtotal = 0


for x in range(3):
    print()
    ytotal = 0
    for y in range(2):
        print()
        ztotal = 0
        for z in range(4):
            vendas +=10
            print(vendas,end=' ')
            total += vendas
            ztotal += vendas
        print()
        print(f'ztotal: {ztotal}')
        ytotal += ztotal
    print()
    print(f'ytotal: {ytotal}')
    xtotal += ytotal
print()
print(f'xtotal: {xtotal}')
print()
print(f'total de vendas: {total}')




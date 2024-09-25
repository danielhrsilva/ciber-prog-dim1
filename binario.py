def binario_para_decimal(binario):
    decimal = int(binario, 2)  # A função int() com base 2 converte binário para decimal
    return decimal

while True:
    binario = input("Digite um número binário: ")
    resultado = binario_para_decimal(binario)
    print(f"O número decimal correspondente é: {resultado}")
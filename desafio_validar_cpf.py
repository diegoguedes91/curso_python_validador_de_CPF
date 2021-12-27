
cpf = input('Entre com o valor do CPF: ')

while len(cpf) != 11 or not cpf.isnumeric() or cpf == cpf[::-1]:
    print(f'O numero {cpf} não é um cpf válido')
    cpf = input('Digite um cpf valido de 11 numeros: ')

soma = 0
cpf_temp = ''
for i, v in enumerate(range(10, 1, -1)):
    mult = v * int(cpf[i])
    soma = soma + mult
    cpf_temp += cpf[i]

digito = 11 - (soma % 11)

if digito > 9:
    digito = 0

cpf_temp = cpf_temp + str(digito)

soma = 0
cpf_valido = ''
for i, v in enumerate(range(11, 1, -1)):
    mult = v * int(cpf_temp[i])
    soma = soma + mult
    cpf_valido += cpf_temp[i]

validade_digito = 11 - (soma % 11)
if validade_digito > 9:
    validade_digito = 0

cpf_valido = cpf_valido + str(validade_digito)


if cpf == cpf_valido:
    print(f'O CPF {cpf} é valido')
else:
    print(f'O CPF {cpf} não é valido')
# Curso de Python 3 do Básico Ao Avançado

#### Desafio :  Validador de CPF

### Ao tentar entrar com um CPF o programa deve fazer de inicio 3 validações: 
* validar se foi digitado 11 caracteres
* checar se a variavel recebida pode ser convertida para numérico 
* verificar se todos os numeros inseridos são diferentes 

```python
cpf = input('Entre com o valor do CPF: ')

while len(cpf) != 11 or not cpf.isnumeric() or cpf == cpf[::-1]:
    print(f'O numero {cpf} não é um cpf válido')
    cpf = input('Digite um cpf valido de 11 numeros: ')
```


### O programa deve ler os 9 primeiros digitos utilizando a regra abaixo e gerar o decimo digito em uma nova variavel :</br>

**CPF USADO NO EXEMPLO:** 168.995350-09 </br>
_obs: CPF gerado aleatoriamente_

1 * 10 = 10</br>
6 * 9  = 54</br>
8 * 8  = 64</br>
9 * 7  = 63</br>
9 * 6  = 54</br>
5 * 5  = 25</br>
3 * 4  = 12</br>
5 * 3  = 15</br>
0 * 2  = 0</br>

soma_de_todos_os_resultados = 297

11 - (297 % 11) 

***Se o resultado for maior que 11 o decimo digito do CPF receberá o valor 0, caso contrario continuara com o valor resultante.***

```python
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
```

### Agora o programa deve criar o digito 11 utilizando as regras abaixo :</br>

1 * 11 = 10</br>
6 * 10  = 54</br>
8 * 9  = 64</br>
9 * 8  = 63</br>
9 * 7  = 54</br>
5 * 6  = 25</br>
3 * 5  = 12</br>
5 * 4  = 15</br>
0 * 3  = 0</br>
0 * 2  = 0</br>

soma_de_todos_os_resultados = 343

11 - (343 % 11) 

***Se o resultado for maior que 11 o decimo primeiro digito do CPF receberá o valor 0, caso contrario continuara com o valor resultante.***

```python
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
```

### Para a ultima etapa basta comparar o CPF digitado com o CPF gerado com o algotimo. 

```python
if cpf == cpf_valido:
    print(f'O CPF {cpf} é valido')
else:
    print(f'O CPF {cpf} não é valido')
  ```

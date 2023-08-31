""" AC2 
Daniel do Nascimento Azevedo
Realizado dia 31/08"""


print("Calculadora salarial")

#Inputs

Funcionário = str(input("Informe o nome de funcionário: "))
setor = str(input("ïnforme o setor do Funcionário: "))
horas_valor = float(input("O valor de salário por hora é: "))
horas_trabalhadas = float(input("Quantas horas trabalhadas no mês: "))


#Conta

salário = horas_valor * horas_trabalhadas


#Prints 

print("O funcionário" ,Funcionário, "do setor" ,setor, "recebe por hora R$" , horas_valor,". O funcionário trabalhou o total de:",horas_trabalhadas, "horas esse mês,o salário do funcionário é: R$",salário,".")



#Exercico 2

print("Calculadora da função")


#Parametros

num1 = 1
num2 = 2
num3 = 3


#Contas

conta1 = (num1 * 2 ) * (0.5 * num3 )
conta2 = (num1 * 3) + num3
conta3 = num3 ** 2


#Prints

print("O resulatado da primeira conta é:",conta1)
print("O resulatado da primeira conta é:",conta2)
print("O resulatado da primeira conta é:",conta3)


# Exercico 3


#Print

print("Calculado interativa função")


#Inputs 

numb1 = float(input("Informe o primeiro valor: "))
numb2 = float(input("Informe o segundo valor: "))
numb3 = float(input("Informe o terceiro valor: "))


#Contas 

resultado1 = (numb1 * 2) * (0.5 * numb3)
resultado2 = (numb2 * 3) + numb3
resultado3 = numb3 ** 2


#Prints

print("O resulatado da primeira conta é:",resultado1)
print("O resultado da segunda conta é:",resultado2)
print("O resultado da terceira conta é:",resultado3)



#Exercicio 4"

#Input

ano = int(input("Informe o ano: "))


#Conta

anocerto = (ano % 4 == 0 and ano %  100 != 0 or ano % 400 == 0)


#Variavél

reposta = "O ano informado é bissexto" if  anocerto else " O ano informado não é bissexto"


#Prints

print(reposta)

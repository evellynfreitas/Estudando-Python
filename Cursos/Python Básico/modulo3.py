print("Tipos de dados")

# int
codigo = 10
print(codigo, "é do tipo:", type(codigo))

# float
salario = 1500.00
print(salario, "é do tipo:",type(salario))

# string
nome = "Jose"
print(nome, "é do tipo:",type(nome))

# boolean
contratado = True
print(contratado, "é do tipo:",type(contratado))

print("---------------------------------------")

print("Código: %d" %codigo)
print("Nome: %s" %nome)
print("Salário: %.2f" %salario)
print("Contratado: %r" %contratado)

print("---------------------------------------")

codigo = int(input("Digite o código: "))
nome = input("Digite o nome: ")
salario = float(input("Digite o salário: "))

print("O funcionário %s possui código %d e recebe R$ %.2f" %(nome,codigo,salario))

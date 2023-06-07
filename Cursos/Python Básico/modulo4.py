#Operadores
A = 3
B = 5
C = 10
D = 15
E = 3

print("A é igual a B? ", A == B)
print("Negação de A é igual a B? ", not A == B)
print("A é menor que B e C? ", A < B and A < C)
print("C é divisível por B? ", C % B == 0)
print("D é divisível por A e B? ", D % B == 0 and D % A == 0)
print("E é igual a A ou a B?", E == A or E == B)
print("---------------------------------------")

#Estruturas de Decisão

idade = 10

if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

idade = 19

if idade >= 18:
    print("maior de idade")
    print("pode dirigir")
    print("pode viajar sozinho")
else:
    print("menor de idade")
    print("não pode dirigir")
    print("não pode viajar sozinho")

print("---------------------------------------")

#Estruturas de Repetição

print("1° for ") # 0 até 9
for i in range(10):
    print(i)
    
print("2° for") # 1 até 10
for i in range(1,11):
    print(i)
    
print("3° for") # 10 até 1
for i in range(10,0,-1):
    print(i)

print("---------------------------------------")

#Estruturas de Repetição: WHILE

x = 0;

while x<5:
    print(x)
    x = x+1
    

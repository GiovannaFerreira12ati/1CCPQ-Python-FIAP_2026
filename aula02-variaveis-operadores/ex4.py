n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
n3=float(input("Digite a nota 3: "))
n4=float(input("Digite a nota 4: "))
n5=float(input("Digite a nota 5: "))

media=(n1+n2+n3+n4)/4

if media >= 7:
    print("Aprovado")
elif media>=5 and media<7:
    print("Em recuperação")
else:
    print("Reprovado")

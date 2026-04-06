n1=float(input("Digite o primeiro valor: "))
n2=float(input("Digite o segundo valor: "))
op=input("Digite o operador")

if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
else:
    print(n1/n2)
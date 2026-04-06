estado=int(input("Digite o código do estado de origem (de 1 a 5:)"))
peso=int(input("Digite o peso em toneladas:"))
codigo=int(input("Digite o código da carga (de 10 a 40):"))

peso_kg=peso*1000

if codigo>=10 and codigo<=20:
    preco=100*peso_kg
elif codigo>=21 and codigo<=30:
    preco=250*peso_kg
else:
    preco=250*peso_kg

if estado == 1:
    imposto=35/100*preco
elif estado==2:
    imposto = 25 / 100 * preco
elif estado==3:
    imposto = 15 / 100 * preco
elif estado==4:
    imposto = 5 / 100 * preco
else:
    imposto = 0

print(f"O peso convertido é {peso_kg}kg")
print(f"O preço da carga do caminhão é R$ {preco}")
print(f"O valor do imposto é {imposto}R$")
print(f"O valor total é {preco+imposto}R$!")
id=int(input("Digite sua idade: "))

if id<16:
    print("Proibido")
elif id>= 16 and id<18:
     print("Opcional")
elif id>=70:
    print("Opcional")
else:
    print("Obrigatório")
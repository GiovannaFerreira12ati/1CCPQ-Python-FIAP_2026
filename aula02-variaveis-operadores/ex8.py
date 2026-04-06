from enum import auto

s=float(input("Digite seu salário:"))

if s<=280:
    aumento=20
elif s>280 and s<=700:
    aumento=15
elif s>700 and s<=1500:
    aumento=10
else:
    aumento=5

v_aumento=aumento/100*s

novo_salario=s+v_aumento

print(s)
print(aumento)
print(v_aumento)
print(novo_salario)
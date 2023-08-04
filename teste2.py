#leia um numero real e armazene o valor em uma viriavel
valor1 = float(input("informe um numero:"))
print(type(valor1))

#verificar se o numero informado é positivo
if valor1>0: #teste for True
    print("o valor informado é positivo!")
elif valor1==0: 
    print("o valor informado é neutro")
else:        #teste for False
    print("o valor informado é negativo!")

print("aqui finaliza o script!!!")    

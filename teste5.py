#leia o valor de um produto caso o valor seja maior do que 100 mostre a seguinte mensagem
#"você recebeu um desconto de 5%", caso contrario
#"você recebeu um desconto de 10%"



valor_prod1 = float(input("informe o valor do produto 1°:"))
valor_prod2 = float(input("informe o valor do produto 2°:"))

if valor_prod1<100:
    print("você recebeu um desconto de 5%")
elif valor_prod1==100:
    print("o valor é neutro nao ganhou nada")
     
else:
    print("vocÊ recebeu um desconto de 10%")


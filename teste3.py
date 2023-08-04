#leia a idade do usuario e informe se ele é maior ou menor de idade

idade = int(input("informe sua idade:"))

if idade>=18:
    print("você é maior de idade")
elif idade<0:
    print("idade invalida")
    print("verifique o valor informado")
else:
    print("você é menor de idade!")
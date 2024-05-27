def menu():

 print("-------------------------------------MENU-------------------------------------")

 print("Bem-vindo ao site Cálculos de: desconto, acréscimo e descoberta de porcentagem.")
 print("                                                                              ")

 print("Lembre-se de inserir apenas o número. Por exemplo, para calcular o desconto, digite 1.")
 print("                                                                              ")

 print("Por favor, informe qual das opções você deseja:")
 print("1 - Desconto")
 print("2 - Acrécimo")
 print("3 - Descoberta de porcentagem")
 print("------------------------------------------------------------------------------")

menu()

x = int(input("Digite o número da sua opção: "))

if x == 1:
 
 def desconto():

    print("                                                                              ")

    percentual = float(input('Coloque o percentual (desconto). Exemplo: Se for 0.15, coloque 15: ')) 

    print("------------------------------------------------------------------------------")

    total = float(input('Coloque o valor que terá o desconto: '))

    parte = (percentual / 100) * total
    valor_com_desconto = total - parte
    
    print("------------------------------------------------------------------------------")

    print('O valor do desconto é:', parte)

    print("------------------------------------------------------------------------------")

    print('O valor final com o desconto aplicado:', valor_com_desconto)

    print("------------------------------------------------------------------------------")

 desconto()
 
elif x == 2:
 
 def acrescimo():

    print("                                                                              ")
    
    percentual = float(input('Coloque o percentual (acréscimo). Exemplo: Se for 0.10, coloque 10: '))

    print("------------------------------------------------------------------------------")

    total = float(input('Coloque o valor que terá o acrécimo: '))

    parte = (percentual / 100) * total
    valor_com_aumento = total + parte

    print("------------------------------------------------------------------------------")

    print('O valor com o aumento:', valor_com_aumento)

    print("------------------------------------------------------------------------------")

 acrescimo()

elif x == 3:
  
 def descobrir_porcentagem():
    
    print("                                                                              ")

    valor_original = float(input("Informe o valor original: "))

    print("------------------------------------------------------------------------------")

    valor_com_desconto = float(input("Informe o valor com o desconto aplicado: "))

    print("------------------------------------------------------------------------------")

    porcentagem_de_desconto = ((valor_original - valor_com_desconto) / valor_original) * 100

    print("------------------------------------------------------------------------------")

    print("O desconto que foi aplicado no valor é: ", porcentagem_de_desconto)

    print("------------------------------------------------------------------------------")

 descobrir_porcentagem()

else:
  
  print("                                                                              ")
  print('Opção invalida! Por favor tente novamente.')
  print("                                                                              ")


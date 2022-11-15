
# Calculadora de CPA de campanhas do dia

print("Bem vido a sistema, insira os numeros para coleta de dados")

vl = float(input("Insira o Valor gasto em ads do dia:"  ))
conv = float(input("Insira quantas vendas voce teve no dia de hoje:"  ))

cpa = vl/conv

print("O seu cpa do dia da campanha selecionada é igual a {}".format(cpa))
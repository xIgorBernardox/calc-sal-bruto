sal_bruto = float(input('Informe o seu salário bruto: \n'))
#Desconto INSS 12%
des_inss = sal_bruto * (12 / 100)
#Desconto Imposto de Renda(IR) 15%
des_ir = sal_bruto * (15 / 100)
#Desconto da Contribuição Sindical obrigatório 8.3%
des_cso = sal_bruto * (8.3 / 100)
#Salário Líquido
sal_liquido = sal_bruto - des_inss - des_ir - des_cso
#Total descontado
total_des = des_inss + des_ir + des_cso
print(f'Seu salário total é: R${sal_bruto}')
print(f'O Desconto do INSS foi de: R${des_inss} / O Desconto do IR foi de: R${des_ir} / O Desconto da contribuição sindical foi de: R${des_cso}')
print(f'O total de descontos foi de: R${total_des}')
print(f'Seu salário Líquido será: R${sal_liquido}')
reis = float(input('Digite seu dinheirus: R$'))
dolls = float(input('Quantos reais está o doll? $'))
conv = reis / dolls
print('Convertendo seus dinherus em \033[34mdolls\033[m, vai dar o volar de \033[34m${:.2f}\033[m dolls.'.format(conv))
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 n�o tem): '))
if dados['ctps'] != 0:
    dados['contrata��o'] = int(input('Ano de contrata��o: '))
    dados['salario'] = float(input('Sal�rio: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrata��o'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k.capitalize()} tem o valor {v}.')
from json import dumps

pessoas = {}
try:
    arquivo = open('users.txt', 'r')  # Transforma o arquivo TXT em dicionário caso exista.
    conteudo = arquivo.readline()
    if len(conteudo) != 0:
        pessoas = eval(conteudo)
except FileNotFoundError:
    arquivo = open('users.txt', 'w')

cor = ('\033[30m',  # branco - 0    # codigos de cores. Estão funcionando
       '\033[31m',  # vermelho - 1
       '\033[32m',  # verde - 2
       '\033[33m',  # amarelo - 3
       '\033[34m',  # azul - 4
       '\033[35m',  # roxo - 5
       '\033[36m',  # azul claro - 6
       '\033[37m',  # cinza - 7
       '\033[m'  # sem cor - 8
       )


def dict_to_txt():  # Transforma o dicionário em TXT
    arquivo = open('users.txt', 'w')
    pessoasstring = dumps(pessoas)
    conteudo = pessoasstring
    arquivo.writelines(conteudo)
    arquivo.close()


def cadastrar_pessoa():  # Cadastra 1 ou mais pessoas em um dicionário, e deixa pronto para visualizar ou salvar
    if len(pessoas.values()) >= 1:
        nomes = list()
        idades = list()
        nomes = pessoas['nome']
        idades = pessoas['idade']
    else:
        nomes = []
        idades = []
    while True:
        r = range(0, 10)
        nome = str(input('\nNome: ')).strip().replace('  ', ' ').title()
        for c in range(0, 10):
            nome = nome.replace(f'{c}', '')
        nome = nome.title()
        if nome.isnumeric() or nome == '':
            print(f'{cor[1]}Digite um nome válido!{cor[8]}')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except Exception:
            print(f'{cor[1]}Digite um valor válido!{cor[8]}')
        else:
            if 121 > idade > 0 != len(nome):
                while True:
                    save = str(input(f'Deseja cadastrar {nome} na lista? [S/N]: ')).strip().lower()
                    if save == 's':
                        nomes.append(nome)
                        idades.append(idade)
                        break
                    elif save == 'n':
                        break
                    else:
                        print(f'{cor[1]}OPÇÃO INVÁLIDA! DIGITE APENAS "S" OU "N"!{cor[8]}')
                break
            else:
                print(f'{cor[1]}IDADE INVÁLIDA. DIGITE NOVAMENTE!{cor[8]}')
    pessoas['nome'] = nomes[:]
    pessoas['idade'] = idades[:]


def ver_grupo():  # Visualiza as pessoas cadastradas
    try:
        len(pessoas['nome'])
    except KeyError:
        print('\n\033[1;31mNÃO EXISTEM PESSOAS CADASTRADAS NO MOMENTO!\033[m')
    else:
        print('--' * 20)
        print('           PESSOAS CADASTRADAS')
        print('--' * 20)
        for c in range(0, len(pessoas['nome'])):
            print(pessoas['nome'][c], end='\t\t\t')
            print(f'{pessoas["idade"][c]:>6} anos')


while True:  # PARTE CORE DO PROGRAMA COM AS CHAMADAS DE FUNÇÕES
    print('--' * 20)
    print('             MENU PRINCIPAL')
    print('--' * 20)
    print(f'''{cor[3]}1{cor[8]}{cor[4]} - Ver pessoas cadastradas{cor[8]}
{cor[3]}2{cor[8]}{cor[4]} - Cadastrar nova pessoa{cor[8]}
{cor[3]}3{cor[8]}{cor[4]} - Sair do sistema{cor[8]}
    ''')
    op = int(input('\033[32mSua opção: \033[m'))
    if op == 3:
        while True:
            salvar = str(input('Deseja salvar novos cadastros realizados? [S/N]: ')).lower().strip()
            if salvar == 's':
                dict_to_txt()
                break
            elif salvar == 'n':
                break
            else:
                print(f'{cor[1]}OPÇÃO INVÁLIDA! DIGITE APENAS "S" OU "N"!{cor[8]}')
        break
    elif op == 2:
        cadastrar_pessoa()
    elif op == 1:
        ver_grupo()
    else:
        print(cor[3], 'OPÇÃO INVÁLIDA!', cor[8])
alunos = [[], [], []]
notas = []
while True:
    nome = str(input('Digite o nome do aluno: ')).title().strip()
    nt1 = float(input('Digite a primera nota: '))
    nt2 = float(input('Digite a segunda nota: '))
    med = (nt1 + nt2) / 2
    notas.append(nt1)
    notas.append(nt2)
    alunos[0].append(nome)
    alunos[1].append(notas[:])
    alunos[2].append(med)
    notas.clear()
    con = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    while con not in 'SN':
        print('Opção inválida! Digite novamente: ', end='')
        con = str(input()).upper().strip()
        if con in 'SN':
            break
    if con == 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>15}')
for c, d in enumerate(alunos[0]):
    print(f'{c:<4}{d:<10}{alunos[2][c]:>15.1f}')
print('-='*20)
while True:
    print('Digite 999 para sair a qualquer momento!')
    mostrar = int(input('Mostrar notas de qual aluno?: '))
    if mostrar == 999:
        break
    print('-'*40)
    print(f'As notas do(a) aluno(a) {alunos[0][mostrar]} foram {alunos[1][mostrar]}.')
    print('-'*40)
aluno = {}

nome = str(input('Digite um nome: ')).title().strip()
nt1 = int(input('Digite a primeira nota: '))
nt2 = int(input('Digite a segunda nota: '))

media = (nt1 + nt2) / 2

if media >= 7:
    st = 'APROVADO'
else:
    st = 'REPROVADO'

aluno['nome'] = nome
aluno['media'] = media
aluno['sit'] = st

print(f'O aluno {aluno["nome"]} conseguiu m�dia {aluno["media"]:.1f}. Est� {aluno["sit"]}!')
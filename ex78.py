nums = list()
for c in range(0, 5):
    nums.append(int(input(f'Digite um n�mero na posi��o {c}: ')))
print(f'Menor valor digitado foi {min(nums)}, na posi��o', end=' ')
menor = min(nums)
for c, f in enumerate(nums):
    if f == menor:
        print(c, end=' ')
print(f'Maior valor digitado foi {max(nums)}, na posi��o', end=' ')
maior = max(nums)
for c, f in enumerate(nums):
    if f == maior:
        print(c, end=' ')
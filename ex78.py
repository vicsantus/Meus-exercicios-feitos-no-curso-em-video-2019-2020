nums = list()
for c in range(0, 5):
    nums.append(int(input(f'Digite um número na posição {c}: ')))
print(f'Menor valor digitado foi {min(nums)}, na posição', end=' ')
menor = min(nums)
for c, f in enumerate(nums):
    if f == menor:
        print(c, end=' ')
print(f'Maior valor digitado foi {max(nums)}, na posição', end=' ')
maior = max(nums)
for c, f in enumerate(nums):
    if f == maior:
        print(c, end=' ')
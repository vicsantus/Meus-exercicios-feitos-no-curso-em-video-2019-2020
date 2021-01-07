from time import sleep
import emoji
c = int(input('Digite um número: '))
for n in range(c, 0, -1):
    print(n)
    sleep(1)
print(emoji.emojize(':fireworks:', use_aliases=True)*10)
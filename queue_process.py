from collections import deque

entrada = input()

palavras = entrada.split()

queue = deque(reversed(palavras))

print(f"deque({list(queue)})")

for palavra in palavras:
    if 'o' in palavra.lower():
        print(palavra)
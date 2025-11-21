from collections import deque

entrada = input()

numeros = list(map(int, entrada.split()))

stack = deque(numeros)

print(f"deque({list(stack)})")

while stack:
    valor = stack.pop()
    print(valor ** 2)

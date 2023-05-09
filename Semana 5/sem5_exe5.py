import random

def busca_bin(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if x == l[meio]:
        return meio

    if x < l[meio]:
        return busca_bin(l, x, inicio, meio -1)

    if x > l[meio]:
        return busca_bin(l, x, meio + 1, fim)

    l = random.sample(range(100), 20)

    l.sort()

    busca_bin(l, 73, 0, 19)

    print(l)
"""O HeapSort é um algoritmo de ordenação que utiliza uma estrutura de dados conhecida como Heap.
O Heap é uma árvore binária completa que pode ser representada em forma de array.
O algoritmo HeapSort consiste em transformar o array desordenado em uma Heap,
em seguida, retirar o elemento raiz (maior valor) e colocá-lo na posição correta. Esse
processo é repetido até que todos os elementos estejam ordenados."""

def heapify(arr, n, i):
    # inicializa o maior como sendo o nó raiz
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # verifica se a subárvore esquerda é maior que a raiz
    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda

    # verifica se a subárvore direita é maior que a raiz
    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    # troca a raiz se necessário
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]

        # heapify a subárvore afetada
        heapify(arr, n, maior)

def heapSort(arr):
    n = len(arr)

    # cria um max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # extrai elementos um por um
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # troca
        heapify(arr, i, 0)

# exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Array ordenado:")
print(arr)

"""O algoritmo começa criando um max heap a partir do array desordenado. 
Em seguida, extrai os elementos um por um, colocando-os na posição correta 
e heapificando a subárvore afetada. No final, o array estará ordenado de forma crescente."""
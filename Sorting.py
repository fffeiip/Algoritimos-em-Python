def insertion_sort(lista):
    for i in range(1, len(lista)):  # percorre de 1 ate o final da lista
        chave = lista[i]  # recebe o elemento atual da lista
        k = i
        # enquanto o valor atual for menor que o valor anterior
        while k > 0 and chave < lista[k-1]:
            lista[k] = lista[k-1]
            k -= 1
        lista[k] = chave  # insere na posição ordenada
    return lista


def quick_sort(lista):
    if len(lista) == 0:
        return lista
    pivot = len(lista)//2
    left = [x for x in lista if x < lista[pivot]]
    meio = [x for x in lista if x == lista[pivot]]    
    right = [x for x in lista if x > lista[pivot]]
    
    return quick_sort(left) +meio+ quick_sort(right)


def teste(x):
    lista = [1, 4, 5, 77, 6, 55, 4, 3, 333, 3, 22, 1, 12, 2, 2, 1]
    print(lista)

    print({
        'insertion_sort': insertion_sort(lista),
        'quick_sort': quick_sort(lista)
    }[x])


teste('quick_sort')
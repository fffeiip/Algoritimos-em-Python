def insertion_sort(lista):
    for i in range(1, len(lista)):  
        chave = lista[i]  
        k = i
        while k > 0 and chave < lista[k-1]:
            lista[k] = lista[k-1]
            k -= 1
        lista[k] = chave  
    return lista


def quick_sort(lista):
    if len(lista) == 0:
        return lista
    pivot = len(lista)//2
    left = [x for x in lista if x < lista[pivot]]
    meio = [x for x in lista if x == lista[pivot]]    
    right = [x for x in lista if x > lista[pivot]]
    
    return quick_sort(left) +meio+ quick_sort(right)

def counting_sort(lista):
    count = []
    for i in range(10):
        count.append(0)     
    for y in lista:
        count[y] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for x in lista:
        index = count[x-1]
        lista[index] = x
    return lista
   
   
def teste(x):
    lista = [1, 4, 5, 3, 1, 1, 2, 2, 1]
    print(lista)

    print({
        'insertion_sort': insertion_sort(lista),
        'quick_sort': quick_sort(lista),
        'counting_sort': counting_sort(lista)
    }[x])


teste('counting_sort')
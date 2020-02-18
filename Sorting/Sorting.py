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
    max_value = max(lista)
    lista_copia = lista.copy()
    for i in range(max_value + 1):
        count.append(0)    
    for y in lista:
        count[y] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for x in lista_copia:
        index = count[x]
        lista[index-1] = x
        count[x] -= 1
    return lista
   
def bubble_sort(lista):
    for x in range(1,len(lista)):
        if lista[x-1] > lista[x]:
            lista[x-1],lista[x] = lista[x],lista[x-1]
            bubble_sort(lista)
    return lista

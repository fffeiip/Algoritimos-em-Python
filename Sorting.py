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
    print(lista)
    if len(lista) == 0:
        return lista
    pivot = len(lista)//2
    left = [x for x in lista if x < lista[pivot]]
    meio = [x for x in lista if x == lista[pivot]]    
    right = [x for x in lista if x > lista[pivot]]
    
    return quick_sort(left) +meio+ quick_sort(right)


def counting_sort(lista):
    # maxQtdCaracteres = len(str(max(lista)))
    # limite = ""
    # for iterator in range(maxQtdCaracteres):
    #     limite += "9"
    count = []
    for i in range(10):
        # for i in range(int(limite)):
        count.append(0)    
    for y in lista:
        count[y] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    print(count)
    for x in lista:
        print("X in lista")
        print(x)
        print("count[x-1]:")
        print(count[x-1])
        index = count[x-1]
        print("index")
        print(index)
        lista[index] = x
        print(lista)
    print(lista)
    # return lista
   
def bubble_sort(lista):
    print(lista)
    for x in range(1,len(lista)):
        if lista[x-1] > lista[x]:
            lista[x-1],lista[x] = lista[x],lista[x-1]
            bubble_sort(lista)
    return lista

def teste(x):
    lista = [1, 4, 5, 3, 1, 1, 2, 29,2,3,455,6,7,788,7,6,55,4,6,7,55,3,21,4,2,6,76767,27,2557,45,323,24,465,75,76,33,225,52,56,7,6,45,2,45,44,24,24234,234,334423,423432,43, 1]
    print(lista)
    # O dicionario tá ordenando a lista automaticamente pq herda da superclasse - @TODO Mudar teste
    # https://docs.python.org/3/library/collections.html#collections.OrderedDict
    print({
        'insertion_sort': insertion_sort(lista),
        'quick_sort': quick_sort(lista),
        'counting_sort': counting_sort(lista),
        'bubble_sort': bubble_sort(lista)
    }[x])


counting_sort([3,4,1,2,2,3,5,4,2])
# teste('bubble_sort')
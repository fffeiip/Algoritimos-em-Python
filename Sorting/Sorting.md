# Sorting

### <a name="counting"></a>Counting Sort


#### O Counting sort é um algoritimo de ordenação de inteiros que assume cada um dos elementos da lista tem uma chave cujo valor está dentro de um intervalo máximo, ou seja, chaves que podem se repetir e que seu valor seja inferior ao maior elemento da lista. Ele funciona contando a quantidade de repetições dos elementos com chaves distintas e depois realiza um cálculo aritimético para determinar o posicionamento na lista ordenada.

* O counting sort é eficiente se o intervalo de valors não for significativamente maior que o número de objetos ordenados.
* Não é uma ordenação baseada em comparações. Ele executa em complexidade O(n), com espaço proporcional ao intervalo de dados.
* É comumente utilizado como sub-rotina de outro algorítimo de ordenação, tipo o [radix sort](#radix).
* O Counting sort utiliza uma técnica de hashing parcial para contar as ocorrencias dos elementos na lista.
* O Counting sort pode ser modificado para funcionar com inputs negativos.

```python 
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
```



Melhor Caso| Caso Médio | Pior Caso | Complexidade de Espaço  
------- | ------- |----|-------
O(k+n) | O(k+n) | O(k+n) |O(k+n)


### <a name="radix"></a> Radix Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:

### <a name="bubble"></a> Bubble Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:

### <a name="insertion"></a> Insertion Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:

### <a name="quick"></a> Quick Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:
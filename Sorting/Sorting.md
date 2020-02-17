# Sorting

### <a name="counting"></a>Counting Sort


#### O Counting sort é um algoritimo de ordenação de inteiros. Ele funciona contando a quantidade de repetições dos elementos dentro de um intervalo [0,k] = {k ∈ N }, onde k é o maior elemento da lista. Em seguida, realiza um cálculo aritimético para determinar o posicionamento do elemento na lista ordenada.

* O counting sort é eficiente se o intervalo de valores não for significativamente maior que o número de objetos ordenados.
* Não é uma ordenação baseada em comparações. Ele executa em complexidade O(n), com espaço proporcional ao intervalo de dados.
* É comumente utilizado como sub-rotina de outro algorítimo de ordenação, e.g. [radix sort](#radix).
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

[logo]: https://github.com/fffeiip/Algoritimos-em-Python/tree/master/Sorting/assets/hrUDdYC7OH-countingsort.gif "Counting Sort"

Reference-style: 
![alt text][logo]



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
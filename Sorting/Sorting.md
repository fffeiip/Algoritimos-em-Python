# Sorting


### <a name="bubble"></a> Bubble Sort
#### O bubble sort é conhecido por ser um algoritimo de força bruta, ele funciona percorrendo todos os elementos da lista, comparando os elementos adjacentes e trocando aqueles que estejam fora de ordem. 

* Se a lista a ser ordenada possui n elementos, ele a percorre n-1 vezes.
* O algoritimo é conhecido como bubble sort porquê para cada iteração, o elemento de maior valor é movido ao final da lista, trocando de posição 1 a 1, como bolhas emergindo à superfície. 

```python
def bubble_sort(lista):
    for x in range(1,len(lista)):
        if lista[x-1] > lista[x]:
            lista[x-1],lista[x] = lista[x],lista[x-1]
            bubble_sort(lista)
    return lista
```

[bubble_sort]: https://github.com/fffeiip/Algoritimos-em-Python/raw/master/Sorting/assets/bubblesort.gif "Bubble Sort"

![Bubble Sort ][bubble_sort]


Melhor Caso| Caso Médio | Pior Caso | Complexidade de Espaço  
------- | ------- |----|-------
O(n) | O(n²) | O(n²) |O(1)


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

[counting_sort]: https://github.com/fffeiip/Algoritimos-em-Python/raw/master/Sorting/assets/countingsort.gif "Counting Sort"

![Couting Sort ][counting_sort]


Melhor Caso| Caso Médio | Pior Caso | Complexidade de Espaço  
------- | ------- |----|-------
O(k+n) | O(k+n) | O(k+n) |O(k+n)



### <a name="quick"></a> Quick Sort
#### O Quick sort é um algoritimo que utiliza a técnica de divisão e consquista, que consiste em recursivamente dividir um problema em subproblemas e resolvê-los, até que o problema principal possa ser resolvido. Na estratégia do algoritimo, um elemento pivô é selecionado e os outros elementos com valores inferiores a ele são recursivamente ordenados e concatenados à sua esquerda enquanto os elementos com valores maiores são ordenados e concatenados à sua direita.

* Existem diversas estratégias para selecionar o elemento pivô 
    * Elemento do meio
    * Primeiro elemento
    * Ultimo elemento
    * Elemento aleatório 
* O quicksort é bem lento para seu pior caso, contudo, para o melhor caso e o caso médio é um algorítimo veloz. 

``` python
def quick_sort(lista):
    if len(lista) == 0:
        return lista
    pivot = len(lista)//2
    esquerda = [x for x in lista if x < lista[pivot]]
    meio = [x for x in lista if x == lista[pivot]]    
    direita = [x for x in lista if x > lista[pivot]]
    
    return quick_sort(esquerda) +meio+ quick_sort(direita)
 ```


[quick_sort]: https://github.com/fffeiip/Algoritimos-em-Python/raw/master/Sorting/assets/quicksort.gif "Quick Sort"

![Quick Sort ][quick_sort]


Melhor Caso| Caso Médio | Pior Caso | Complexidade de Espaço  
------- | ------- |----|-------
O(n log n) | O(n log n) | O(n²) |O(n)


### <a name="radix"></a> Radix Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:




### <a name="insertion"></a> Insertion Sort
#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:construction: :construction:

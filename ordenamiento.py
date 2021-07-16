"""
╔════════════════════════════════╗
║  ALGORITMOS DE ORDENAMIENTO    ║
╠════════════════════════════════╣
║ Burbuja (BubleSort)            ║
║ Selección (SelectionSort)      ║
║ Inserción (insertionSort)      ║
║ Inserción Binaria              ║
║ Shell                          ║
║ Rápido                         ║
║ Merge                          ║
╚════════════════════════════════╝
"""


def BubleSort(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(i+1,n):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def SelectionSort(lista):
    n=len(lista)
    for i in range(n):
        menor=i
        for j in range(i+1,n):
            if lista[j]<lista[menor]:
                menor=j
        lista[i],lista[menor] = lista[menor],lista[i]
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        num = lista[i]
        j = i-1
        while j >=0 and num < lista[j] :
                lista[j+1] = lista[j]
                j -= 1
        lista[j+1] = num
    return lista

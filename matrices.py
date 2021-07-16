
matriz=[]

# lleno la matriz
k=1
for a in range(0,3):
    fila=[]
    for b in range(0,3):
        fila.append(k)
        k+=1
    matriz.append(fila)

#imprimo la matriz
print("Impresión de la matriz")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()

print("suma de los valores de las filas y columnas de la matriz")
# suma los valores de la filas
for a in range(len(matriz)):
    suma_fila = 0
    for b in range(len(matriz[a])):
        suma_fila += matriz[a][b]
    print(matriz[a],end="")
    print(suma_fila)

#suma las columnas
suma_columnas = []
for a in range(len(matriz)):
    suma = 0
    for b in range(len(matriz[a])):
        suma += matriz[b][a]
    suma_columnas.append(suma)
print(*suma_columnas)

print("Suma de los valores de las diagonales de la matriz ")
# suma la diagonal
suma_diagonal = 0
for a in range(len(matriz)):
    suma_diagonal += matriz[a][a]
print("suma_diagonal=",suma_diagonal)

# suma la diagonal inversa
suma_diagonal_inversa = 0
for a in range(len(matriz)):
    suma_diagonal_inversa+=matriz[a][len(matriz)-1-a]

print("suma_diagonal_inversa=",suma_diagonal_inversa)

# suma todos lo elementos de la matríz
print("Suma de todos los elementos de la matriz")
suma = 0
for a in range(len(matriz)):
    for b in range(len(matriz[a])):
        suma+=matriz[a][b]

print("suma de toda la matriz", suma)

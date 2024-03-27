#TALLER 1
#PUNTO 1
a = [1, 2, 3]
b = [3, 4, 5]
def suma_de_vectores(a,b):
  return [x + y for x, y in zip(a, b)] 
def resta_de_vectores(a,b):
  return [x - y for x, y in zip(a, b)] 
def ppunto_de_vectores(a,b):
  return sum(x * y for x, y in zip(a, b)) 
def pcruz_de_vectores(a,b):
  return [a[1]*b[2]-b[1]*a[2],-(a[0]*b[2]-b[0]*a[2]),a[0]*b[1]-b[0]*a[1]]
def division_de_vectores(a,b):
  return [x / y for x, y in zip(a, b)]
print("suma: ", suma_de_vectores(a,b))
print("resta: ", resta_de_vectores(a,b))
print("producto punto: ", ppunto_de_vectores(a,b))
print("producto cruz: ", pcruz_de_vectores(a,b))
print("division: ", division_de_vectores(a,b))

#PUNTO 2
c = ([1, 2, 3],[4,5,6],[7,8,9])
d = ([3, 4, 5],[6,7,8],[9,10,11])
def sum_matrices(c, d):
    result = []
    for i in range(len(c)):
        row = []
        for j in range(len(c[0])):
            row.append(c[i][j] + d[i][j])
        result.append(row)
    return result
sum_result = sum_matrices(c, d)
print("Suma de matrices:")
for row in sum_result:
    print(row)

c = ([1, 2, 3],[4,5,6],[7,8,9])
d = ([3, 4, 5],[6,7,8],[9,10,11])
def sum_matrices(c, d):
    result = []
    for i in range(len(c)):
        row = []
        for j in range(len(c[0])):
            row.append(c[i][j] - d[i][j])
        result.append(row)
    return result
sum_result = sum_matrices(c, d)
print("Resta de matrices:")
for row in sum_result:
    print(row)
###########################################################################################
def producto_punto_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
# Ejemplo de uso
matriz_A = [[1, 2, 3],[4,5,6],[7,8,9]]
matriz_B = [[3, 4, 5],[6,7,8],[9,10,11]]
resultado_producto_punto = producto_punto_matrices(matriz_A, matriz_B)
print("Producto punto de las matrices A y B:")
for fila in resultado_producto_punto:
    print(fila)
############################################################################################
def producto_cruz_matrices(matrix1, matrix2):
    if len(matrix1) != 3 or len(matrix2) != 3:
        raise ValueError("Las matrices deben ser de dimensiones 3x3 para el producto cruz.")

    result = [[0] * 3 for _ in range(3)]
    for i in range(3):
        result[i][0] = matrix1[(i + 1) % 3][1] * matrix2[(i + 2) % 3][2] - matrix1[(i + 2) % 3][1] * matrix2[(i + 1) % 3][2]
        result[i][1] = matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][2] - matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][2]
        result[i][2] = matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][1] - matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][1]

    return result

# Ejemplo de uso
matriz_A = [[1, 2, 3],[4,5,6],[7,8,9]]
matriz_B = [[3, 4, 5],[6,7,8],[9,10,11]]
resultado_manual = producto_cruz_matrices(matriz_A, matriz_B)

print("Producto cruz de las matrices A y B:")
for fila in resultado_manual:
    print(fila)


# Mi implementación muy básica de una matriz
class Matriz:
    def __init__(self, filas, columnas, datos=None):
        self.filas = filas
        self.columnas = columnas
        if datos:
            self.datos = datos
        else:
            self.datos = [[0 for _ in range(columnas)] for _ in range(filas)]

    def asignar(self, fila, columna, valor):
        self.datos[fila][columna] = valor

    def obtener(self, fila, columna):
        return self.datos[fila][columna]

    def mostrar(self):
        for fila in self.datos:
            print(fila)

    def multiplicar(self, otra):
        if self.columnas != otra.filas:
            raise ValueError("No se pueden multiplicar: porque los tamaños no son compatibles.")
        
        resultado = Matriz(self.filas, otra.columnas)
        for i in range(self.filas):
            for j in range(otra.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otra.datos[k][j]
                resultado.asignar(i, j, suma)
        return resultado


# Para este ejemplo, investigué que las matrices son muy usadas en los videojuegos, y hay matrices que guardan las propiedades de los
# objetos, como la rotacion, escalados, etc.

# Puntos en un plano 
puntos = Matriz(3, 2, [
    [1, 2],
    [3, 4],
    [5, 6]
])

# Matriz de escalado 2x2
escalado = Matriz(2, 2, [
    [2, 0],
    [0, 2]
])

print("Puntos originales:")
puntos.mostrar()

print("\nMatriz de escalado:")
escalado.mostrar()

# Multiplicación: (3x2) x (2x2) = (3x2)
puntos_escalados = puntos.multiplicar(escalado)

print("\nPuntos escalados (x2):")
puntos_escalados.mostrar()

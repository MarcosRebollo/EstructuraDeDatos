class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, valor):
        self.elementos.append(valor)

    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tiempo_total_atencion(self):
        return sum(self.elementos)

# Para el ejemplo de esta implementación, decidí usar el ejemplo más común de las colas y aplicarlo
# en una cola de espera común. Y como operación, calculé el tiempo de espera que se acumula en la cola
cola = Cola()
cola.encolar(5)  # Cliente 1
cola.encolar(3)  # Cliente 2
cola.encolar(7)  # Cliente 3

print("Tiempo total de atención:", cola.tiempo_total_atencion(), "minutos")

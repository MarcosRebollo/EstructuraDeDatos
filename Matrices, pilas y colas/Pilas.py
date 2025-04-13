# Mi implementaciónn muy basica de una pila
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

# Como cálculo decidí usarla para evaluar expresiones postfijas, ya que investigando
# vi que era un uso de las pilas muy común y que ayuda muchísimo.
def evaluar_postfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            b = pila.desapilar()
            a = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
    return pila.desapilar()

# "3 4 + 2 *" = (3 + 4) * 2 = 14
print("Resultado:", evaluar_postfija("3 4 + 2 *"))

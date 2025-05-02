class Calculadora:
    def _init_(self):
        # Inicializa a calculadora.
        pass

    def adicionar(self, a: float, b: float) -> float:
        # Retorna a soma de dois números.
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        # Retorna a subtração de dois números.
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        # Retorna a multiplicação de dois números.
        return a * b

    def dividir(self, a: float, b: float) -> float:
        # Retorna a divisão de dois números, ou lança um erro se o divisor for zero.
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b




class CalculadoraDiferente:

    def inverte_numero(self, numero):
        numero_invertido = 0
        while numero > 0:
            temp = numero % 10
            numero_invertido = numero_invertido * 10 + temp
            numero = numero // 10
        return numero_invertido
    
    def fatorial(self, numero):
        resultado = 1
        for index in range(1, numero + 1):
            resultado *= index
        return resultado
    
    def soma_dobro(self, a, b):
        return a + b * 2

'''
Aqui eu criei uma classe para rodar o cálculo sequêncial de Fibonacci e verificar se pretence ou não.
Após deifinir minha classe, inicialmente eu crio um método que recebe o número que vou digitar, o elemento descrito no enunciado
e difino o método a seguir que tem por função roda a soma do último com o penúltimo elemento da lista,
pois nessa sequência o valor a seguir é sempre a soma dos dois valores anteriores e isso eu adiciono na lista.
Na verificação ele vai comparar se o número faz parte da sequência e retorna a mensagem se pertence ou não.
Por fim defino um metodo de interação com o usuário, onde eu recebo ele dentro da variável número.
Em seguida chamo o objeto da minha classe que recebe o número escolhido
'''

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.elementos = [0, 1]
        self.calculadora_sequencia()

    def calculadora_sequencia(self):
        while self.elementos[-1] <= self.n:
            self.elementos.append(self.elementos[-1] + self.elementos[-2])
    
    def verificao(self):
        if self.n in self.elementos:
            return f"{self.n} pertence a sequência Fibonocci!"
        else:
            return f"{self.n} não pertence a sequência Fibonocci!"
    
def interacao():
    n = int(input("Digite um número: "))
    return n

numero = interacao()
fibonacci = Fibonacci(numero)
print(fibonacci.verificao())

class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self, x):
        if len(self.data) > 0:
            return self.data.pop[0]

    def empty(self):
        return not len(self.data) > 0

"""f = Fila()
num = 14
while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    print(p.pop()) """


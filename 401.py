class cachorro():
    def __init__(self, nome, especie, patas):
        self.nome = nome 
        self.especie = especie
        self.patas = patas

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

cachorro = cachorro("Bidu", "desenho", "4")
    


print(cachorro.get_nome())

print("meu nome é {} e eu sou um {} de {} patas".format(cachorro.nome, cachorro.especie, cachorro.patas))

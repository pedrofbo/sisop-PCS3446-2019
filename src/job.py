import numpy as np

class Job():

    status = 'inativo'
    #salvos = []

    def __init__(self, nome, nseg, segmentos, prioridade, entradas, saidas, chegada):
        self.nome = nome
        self.nseg = nseg
        self.segmentos = segmentos
        self.prioridade = prioridade
        self.entradas = entradas
        self.saidas = saidas
        self.chegada = chegada

        self.ntotal = 2 + np.random.randint(0, 4)
        if self.ntotal > nseg:
            self.ntotal = nseg

        self.seginit = np.random.randint(2, 5)
        if self.seginit > nseg:
            self.seginit = nseg

        self.salvos = []

        for i in range(0, self.nseg):
            if i == 0:
                self.salvos.append(1)
            elif i == self.seginit - 1:
                self.salvos.append(1)
            else:
                self.salvos.append(0)

        self.count = 0

    def __repr__(self):
        return self.nome

    def describe(self):
        print(f'\nNome: {self.nome}')
        print(f'Instante de chegada: {self.chegada}')
        print(f'Prioridade: {self.prioridade}')
        print(f'Entradas: {self.entradas}   Saidas: {self.saidas}')
        print(f'Numero de segmentos: {self.nseg}')
        print(self.salvos)
        
        print('Segmentos salvos na memoria: \n')
        for i in range(self.nseg):
            if self.salvos[i] == 1:
                print(f'{self.segmentos[i][1:]}     Endereco: {self.segmentos[i][0]}')

        print('Segmentos nao salvos na memoria: \n')
        for i in range(self.nseg):
            if self.salvos[i] == 0:
                print(f'{self.segmentos[i][1:]}     Endereco: {self.segmentos[i][0]}')
        print('\n')

    def estimar(self):
        tempo = 0
        for segmento in self.segmentos:
            tempo += (len(segmento) - 1) * 10
        tempo += (self.entradas + self.saidas) * 50
        return tempo
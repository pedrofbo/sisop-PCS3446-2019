from job import Job
from jobscheduler import decode, schedule
from memory import Memory
import numpy as np

def inicio():
    print('1. Inserir entrada')
    print('2. Configurar simulador')
    print('3. Encerrar simulador')

def memsave(memory, jobs):
    for job in jobs:
        for i in range(job.nseg):
            if job.salvos[i] == 1:
                memory.loadMemory(job.segmentos[i])
    return memory

def randomize(ntotal, nseg):
    ordem = [1]
    while len(ordem) < ntotal:
        prox = np.random.randint(1, nseg + 1)
        if prox not in ordem:
            ordem.append(prox)
    return ordem

def simular(memory, jobs, mult):
    print('\nInicializando simulacao...')
    print(f'Grau de multiprogramacao: {mult}')

    count = 0

    #while count < 


def main():

    mult = 1

    while(1):
        inicio()
        op = input('Escolha uma opcao: ')
        memory = Memory()

        if op == '1':
            entrada = input('Digite o nome de sua entrada: ')

            jobs = decode(entrada + '.txt')
            jobsched = schedule(jobs)

            print(jobsched)
            print('\n')

            for job in jobsched:
                job.describe()

            memory = memsave(memory, jobsched)
            memory.showMemory()

            s = input('\nIniciar simulacao?(y/n): ')
            if s == 'y':
                pass

        
        elif op == '3':
            return 0

if __name__ == "__main__":
    main()
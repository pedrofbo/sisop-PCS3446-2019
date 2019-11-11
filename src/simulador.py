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
    tempoest = 0

    for job in jobs:
        tempoest += job.estimar()

    print(f'Tempo estimado de simulação: {tempoest}')

    while count < tempoest:
        job = jobs[0]

        if count >= job.chegada:
            print(f'\nIniciando processamento de: {job.nome}')
            ordem = randomize(job.ntotal, job.nseg)
            print(f'Segmentos necessarios: {ordem} \n')
            for seg in ordem:
                if job.salvos[seg - 1] == 1:
                    count += (len(job.segmentos[seg - 1]) - 1) * 10
                else:
                    print('\nInterrupcao: segmento nao salvo na memoria\n')
                    print(f'\nInstante: {count} \n')
                    print('\n Salvando segmento faltante... \n')
                    memory.loadMemory(job.segmentos[seg - 1])
                    memory.showMemory()
                    count += (len(job.segmentos[seg - 1]) - 1) * 15
            print(f'\nInstante: {count} \n')

            jobs.pop(0)
            if len(jobs) == 0:
                print(f'\n Fim da simulacao! \nInstante: {count} \n')
                return 0 


        count += 1


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
                simular(memory, jobsched, mult)

        
        elif op == '3':
            return 0

if __name__ == "__main__":
    main()
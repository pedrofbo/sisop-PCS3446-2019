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

    count = jobs[0].chegada
    tempoest = 0
    cjob = []
    ordem = []

    for job in jobs:
        tempoest += job.estimar()

    print(f'Tempo estimado de simulação: {tempoest}')

    while len(jobs) > 0:
        for i in range(mult):
            if len(jobs) > 0:
                cjob.append(jobs[0])
                ordem.append(randomize(jobs[0].ntotal, jobs[0].nseg))
                jobs.pop(0)

        if count >= cjob[0].chegada:
            print(f'\nInstante: {count} \n')
            print('\nIniciando processamento de: ')
            print(cjob)
            for i in range(len(cjob)):
                print(cjob[i].nome)
                print(f'Segmentos necessarios: {ordem[i]} \n')
                cjob[i].count = count

            for i in range(len(cjob)):
                for seg in ordem[i]:
                    if cjob[i].salvos[seg - 1] == 1:
                        cjob[i].count += (len(cjob[i].segmentos[seg - 1]) - 1) * 10
                        print('\nSegmento executado!')
                        print(f'Instante: {cjob[i].count}')
                    else:
                        print('\nInterrupcao: segmento nao salvo na memoria\n')
                        print(f'\nInstante: {cjob[i].count} \n')
                        print('\n Salvando segmento faltante... \n')
                        memory.loadMemory(cjob[i].segmentos[seg - 1])
                        memory.showMemory()
                        cjob[i].count += (len(cjob[i].segmentos[seg - 1]) - 1) * 15
                        print('\nSegmento executado!')
                        print(f'Instante: {cjob[i].count}')
                    if cjob[i].entradas > 0:
                        print('\nInterrupcao: request de entrada\n')
                        print(f'Instate: {cjob[i].count}')
                        print('\nTratando request...\n')
                        cjob[i].entradas -= 1
                        cjob[i].count += 50
                    elif cjob[i].saidas > 0:
                        print('\nInterrupcao: request de entrada\n')
                        print(f'Instate: {cjob[i].count}')
                        print('\nTratando request...\n')
                        cjob[i].saidas -= 1
                        cjob[i].count += 50
            
            
            counts = []
            for i in range(len(cjob)):
                counts.append(cjob[i].count)
            counts.sort()
            count = counts[-1]
            print(f'\nInstante: {count} \n')

            cjob.clear()
            ordem.clear()

    print(f'\n Fim da simulacao! \nInstante: {count} \n')


def main():

    mult = '1'

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
                simular(memory, jobsched, int(mult))

        elif op == '2':
            print(f'Grau de multiprogramacao: {mult}')
            op2 = input('Deseja alterar? (y/n): ')
            if op2 == 'y':
                mult = input('Novo grau de multiprogramacao: ')

        elif op == '3':
            return 0

if __name__ == "__main__":
    main()
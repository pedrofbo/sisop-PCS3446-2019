import pandas as pd
import queue
from job import Job

def decode(entrada):
    jobs = []
    programas = pd.read_csv(entrada, header = None)
    print('\n')
    print(programas)
    print('\n')

    for i in range(0, len(programas[0])):
        segmentos = []
        f = open('disc/' + programas[0][i] + '.txt', "r")
        
        linha1 = f.readline().split()
        nseg = linha1[0]
        prioridade = linha1[1]

        for j in range(0, int(nseg)):
            segmento = f.readline().split()
            segmentos.append(segmento)
    
        job = Job(programas[0][i], int(nseg), segmentos, int(prioridade), int(programas[2][i]), int(programas[3][i]), int(programas[1][i]))
        jobs.append(job)
        f.close()
    
    return jobs

def schedule(jobs):
    jobsin = []
    jobout = []
    q = queue.PriorityQueue()

    for i in range(len(jobs)):
        jobsin.append((jobs[i].prioridade, jobs[i].chegada))

    for job in jobsin:
        q.put(job)

    while not q.empty():
        tp = q.get()
        pr = tp[0]
        ch = tp[1]
        for job in jobs:
            if job.prioridade == pr and job.chegada == ch:
                jobout.append(job)
    
    return jobout
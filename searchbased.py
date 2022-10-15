# This is a sample Python script.
import random

import numpy as np
from numpy.random import rand
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def createpop(npop,chromose):
    pop=np.random.randint(0,2,(npop,chromose))
    return pop
#pop=createpop(20,5)
#print(pop)

def Fitness_Individual(chromose):
    chromosefitness=sum(chromose) # Evaluate fitness of individual
    return chromosefitness


def Fitness_pop(pop,npop):
    popfit=np.zeros(npop)  #array that stores fitness for each individual in population
    for i in range(npop):
        popfit[i]=Fitness_Individual(pop[i]) # to calculate all the individuals in the population
       # print(popfit[i])
    return popfit

def selection_probability(popfit):
    totalfitness=sum(popfit) # Get total sum of all fitness in the population
    probability=[i/totalfitness for i in popfit] # divide each individual with the total fitness
    return probability

def cumulative(probability):
 global cumprop
 cumprop = np.zeros_like(probability)
 cumprop[0]=probability[0]
 for i in range (1,len(probability)):
        cumprop=cumprop[i-1]+probability[i]
        return cumprop

def roulettewheel(cumprop):
    r=np.random.random()
    for i in range(len(cumprop)):
         if r<= cumprop[i]:
            index=i
            return index

##def roulettewheel_select(cumprop,pop):
 #   twoparents=np.zeros((2,np.size(pop,1)))
 #   for i in range(2):
  #      index=roulettewheel(cumprop)
   #     twoparents[i,:]=pop[index,:]
   # return twoparents

def roulettewheel_select(cumprop,pop):
   global parent1,parent2
   parent1=np.zeros(pop)
   parent2=np.zeros(pop)
   for i in range(2):
        index=roulettewheel(cumprop)
        parent1[i,:]=pop[index,:]
        parent2[i,:]=pop[index,:]
   return parent1,parent2


def crossover(parent1,parent2,pcross,chromose):
    child1,child2=parent1.copy,parent2.copy
    if rand() <pcross:
        point=rand() * len(chromose)
        child1=parent1[:point]+parent2[point:]
        child2=parent2[:point]+parent1[point:]
    return [child1,child2]

def mutation(pumte,chromose):
    for i in range(len(chromose)):
        if(random.random() <pumte):
            if(chromose[i]==1):
                chromose[i]=0
            else:
                chromose[i]=1
    return chromose
def Algorithm(npop,iterations,chro_len,prcoss,pmute,fitnesspop):

    pop=createpop(npop,chro_len) #creatation of population
    best=0
    for g in range(iterations):

        values=fitnesspop(pop, npop)
        for i in range(npop):
            if values[i]<best:
                best=pop[i],values[i]
                print(g,pop[i],values[i])
        selected_parents= [roulettewheel_select(cumprop,pop) for _ in range(npop)]
        childs=list()
        for i in range(0,npop,2):
            parent1,parent2=selected_parents[i],selected_parents[i+1]
            for c in crossover(parent1,parent2,pcross,chro_len):
                mutation(pmute,chro_len)
                childs.append(c)
        pop=childs

    return best
iterations=100
chromosome_length=5
npop=20
pcross=0.6
pmute=0.05
result=Algorithm(npop,iterations,chromosome_length,pcross,pmute,Fitness_pop)
print(result)





















    









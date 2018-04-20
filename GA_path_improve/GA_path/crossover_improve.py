# -*- coding: utf-8 -*-

import random

def cal_pc(elder_value, max_value, avg_value):
    kc = 0.8
    if elder_value > avg_value:
        pc = kc * (max_value - elder_value) / (max_value - avg_value)
    else:
        pc = kc

    return pc

def crossover(pop, increment_prob, fit_value, max_value, avg_value):
    for i in range(len(pop)):
        ms1 = random.random()
        ms2 = random.random()
        father_num = 0
        mother_num = 0
        father = pop[0]
        mother = pop[0]

        for i in range(len(pop)):
            if increment_prob[i - 1] <= ms1 <increment_prob[i]:
                father_num = i
                father = pop[i]
            if increment_prob[i - 1] <= ms2 <increment_prob[i]:
                mother_num = i
                mother = pop[i]

        pc = cal_pc(max(fit_value[father_num], fit_value[mother_num]), max_value, avg_value)
        if(pc > random.random()):
            cpoint = random.randint(0,len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(father[0:cpoint])
            temp1.extend(mother[cpoint:len(mother)])
            temp2.extend(mother[0:cpoint])
            temp2.extend(father[cpoint:len(father)])
            pop[father_num] = temp1
            pop[mother_num] = temp2

    return pop

if __name__ == '__main__':
    pass
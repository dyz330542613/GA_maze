# -*- coding: utf-8 -*-

import random

def mutation(pop, pm):
    for i in range(len(pop)):
        if(pm[i] > random.random()):
            mpoint = random.randint(0, len(pop[0]) - 1)
            gpoint = random.randint(0, 1)
            if(pop[i][mpoint][gpoint] == 1):
                pop[i][mpoint][gpoint] = 0
            else:
                pop[i][mpoint][gpoint] = 1

    return pop

if __name__ == '__main__':
    pass
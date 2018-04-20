# -*- coding: utf-8 -*-

import random

def geneEncoding(pop_size, chrom_length):
    pop = []
    for i in range(pop_size):
        direction = []
        for j in range(chrom_length):
            temp = []
            temp.append(random.randint(0, 1))
            temp.append(random.randint(0, 1))
            direction.append(temp)
        pop.append(direction)  # [0, 0] up, [0, 1] down, [1, 0] left, [1, 1] right
    return pop

if __name__ == '__main__':
    pass
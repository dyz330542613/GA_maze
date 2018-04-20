# -*- coding: utf-8 -*-
# find the best fitness value, the best individual and the best path

def best(pop, fit_value, path):

    best_individual = []
    best_individual.append(pop[0])
    best_fit = fit_value[0]
    best_path = []
    best_path.append(path[0])
    for i in range(len(pop)):
        if(fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual.append(pop[i])
            best_path.append(path[i])

    return best_fit, best_individual[-1], best_path[-1]

if __name__ == '__main__':
    pass
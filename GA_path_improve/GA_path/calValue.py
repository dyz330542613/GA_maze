# -*- coding: utf-8 -*-

def calValue(path, maze_wide, maze_high):
    fit_value = []
    for i in range(len(path)):
        obj_value = path[i][-1]
        fit_value.append(1 / ((maze_wide - obj_value[0]) + (maze_high - obj_value[1])))

    avg_value = sum(fit_value) / len(fit_value)
    return fit_value, avg_value

if __name__ == '__main__':
    pass
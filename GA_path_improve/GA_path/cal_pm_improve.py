# -*- coding: utf-8 -*-
# calculate mutation rate

def cal_pm(fit_value, max_value, avg_value):
    pm = []
    km = 0.5
    for i in range(len(fit_value)):
        if fit_value[i] > avg_value:
            pm.append(km * (max_value - fit_value[i]) / (max_value - avg_value))
        else:
            pm.append(km)

    return pm
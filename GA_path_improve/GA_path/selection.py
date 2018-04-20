# -*- coding: utf-8 -*-

def sum(fit_value):
	total = 0
	for i in range(len(fit_value)):
		total += fit_value[i]
	return total

def cumsum(fit_value):
	for i in range(len(fit_value)-2, -1, -1):
		t = 0
		j = 0
		while(j <= i):
			t += fit_value[j]
			j += 1
		fit_value[i] = t
		fit_value[len(fit_value) - 1] = 1


def selection(fit_value):
	newfit_value = []
	total_fit = sum(fit_value)
	for i in range(len(fit_value)):
		newfit_value.append(fit_value[i] / total_fit)
	cumsum(newfit_value)

	# ms = []
	# pop_len = len(pop)
	# for i in range(pop_len):
	# 	ms.append(random.random())
	# ms.sort()
	# fitin = 0
	# newin = 0
	# newpop = pop

	u'''Roulette Algorithm'''
	# while newin < pop_len:
	# 	if(ms[newin] < newfit_value[fitin]):
	# 		newpop[newin] = pop[fitin]
	# 		newin = newin + 1
	# 	else:
	# 		fitin = fitin + 1

 	# ms1 = random.random()
	# ms2 = random.random()
	# elder = []
	# for i in range(len(fit_value)):
	# 	if ms1 > newfit_value[i - 1] and ms1 < newfit_value[i]:
	# 		elder.append(pop[i])
	# 	if ms2 > newfit_value[i - 1] and ms2 < newfit_value[i]:
	# 		elder.append(pop[i])

	return newfit_value

if __name__ == '__main__':
	pass
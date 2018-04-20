# -*- coding: utf-8 -*-

import random
from tkinter import *
import time

import numpy
import matplotlib
matplotlib.use('TkAgg')

from GA_path.best import best
from GA_path.calValue import calValue
from GA_path.cal_pm import cal_pm
from GA_path.crossover import crossover
from GA_path.geneEncoding import geneEncoding
from GA_path.mutation import mutation
from GA_path.selection import selection


class base_maze_grid(object):

	def __init__(self):
		self.access = False
		self.up = False
		self.down = False
		self.left = False
		self.right = False


class generate_maze(object):

	def __init__(self, wide=10, high=10):
		self.wide = wide
		self.high = high
		self.root = Tk()
		self.pop = []
		self.show_maze_gui()

	def init_maze(self):

		u'''initialize maze'''

		self.maze = list()
		self.maze_path = []
		self.wide = int(self.grid_sum.get())
		self.high = int(self.grid_sum.get())


		for i in range(self.high):
			temp = []
			for i1 in range(self.wide):
				temp.append(base_maze_grid())
			self.maze.append(temp)

	def mode_recursive_backtracker(self):

		u'''Backtracking Algorithm'''

		self.init_maze()

		history = list()
		current = (0, 0)
		self.maze[current[0]][current[1]].access = True

		while len([False for i in self.maze for i1 in i if i1.access == False]) > 0:
			adjacent_grid = self.get_adjacent_grid(current)
			if adjacent_grid:
				new_grid = random.choice(adjacent_grid)
				history.append(current)
				self.get_through(current, new_grid)
				current = new_grid
				self.maze[current[0]][current[1]].access = True
			elif history:
				current = history.pop()
			if not self.maze_path:
				if current == (self.wide - 1, self.high - 1):
					self.maze_path = history[:]
					self.maze_path.append(current)
				# print len(self.maze_path)

		self.draw_maze()

	def get_adjacent_grid(self, xy):

		u'''get unvisited grids in 4 directions'''

		temp = []
		for xy_int in [(xy[0] + 1, xy[1]), (xy[0] - 1, xy[1]), (xy[0], xy[1] + 1), (xy[0], xy[1] - 1)]:
			if 0 <= xy_int[0] <= self.wide - 1 and 0 <= xy_int[1] <= self.high - 1:
				if not self.maze[xy_int[0]][xy_int[1]].access:
					temp.append(xy_int)

		return temp

	def get_through(self, a, b):

		u'''get through walls'''

		if a[0] < b[0]:
			self.maze[a[0]][a[1]].right = True
			self.maze[b[0]][b[1]].left = True
		elif a[0] > b[0]:
			self.maze[a[0]][a[1]].left = True
			self.maze[b[0]][b[1]].right = True

		if a[1] < b[1]:
			self.maze[a[0]][a[1]].down = True
			self.maze[b[0]][b[1]].up = True
		elif a[1] > b[1]:
			self.maze[a[0]][a[1]].up = True
			self.maze[b[0]][b[1]].down = True


	def show_maze_gui(self):

		u'''display maze interface'''

		self.root.title('Maze')
		self.cwidth = 750
		self.cheight = 750
		control1 = LabelFrame(self.root)
		control1['text'] = u'Number of Grids'
		default_value = StringVar()
		default_value.set('10')
		self.grid_sum = Entry(control1, textvariable=default_value)
		self.grid_sum.pack(side=LEFT, expand=YES, fill=X)
		control1.pack(fill=X, padx=5, pady=5)
		control = LabelFrame(self.root)
		control['text'] = u'Maze Console'
		self.start = Button(control, text=u'Initialize Maze', command=self.mode_recursive_backtracker)
		self.start.pack(fill=X)
		self.show_path = Button(control, text=u'Display Path', command=self.draw_path)
		self.show_path.pack(side=LEFT, expand=YES, fill=X)
		self.show_path = Button(control, text=u'Hide Path', command=self.draw_maze)
		self.show_path.pack(side=LEFT, expand=YES, fill=X)
		control.pack(fill=X, padx=5, pady=5)
		self.canvas = Canvas(self.root, width=self.cwidth + 1, height=self.cheight + 1, bg='white')
		self.canvas.pack()
		self.mode_recursive_backtracker()
		self.root.mainloop()

	def draw_maze(self):

		u'''draw maze'''

		self.canvas.create_rectangle(0, 0, self.cwidth + 5, self.cheight + 5, fill='white')
		xspacing = self.cwidth / self.wide
		yspacing = self.cheight / self.high
		self.maze[0][0].left = True
		self.maze[-1][-1].right = True

		a_x = 2
		a_y = 2
		self.temp = {}


		for x, i in enumerate(self.maze):
			for y, i1 in enumerate(i):
				if not self.maze[x][y].up:
					self.canvas.create_line(a_x, a_y, a_x + xspacing, a_y)
				if not self.maze[x][y].down:
					self.canvas.create_line(a_x, a_y + yspacing, a_x + xspacing, a_y + yspacing)
				if not self.maze[x][y].left:
					self.canvas.create_line(a_x, a_y, a_x, a_y + yspacing)
				if not self.maze[x][y].right:
					self.canvas.create_line(a_x + xspacing, a_y, a_x + xspacing, a_y + yspacing)
				if (x, y) in self.maze_path:
					# self.canvas.create_oval(a_x+(xspacing/4), a_y+(yspacing/4), a_x+xspacing-xspacing/4, a_y+yspacing-yspacing/4, fill = "green")
					self.temp[(x, y)] = (a_x + xspacing / 2, a_y + yspacing / 2)
				# if (x, y) in self.new_maze_path:
				# 	# self.canvas.create_oval(a_x+(xspacing/4), a_y+(yspacing/4), a_x+xspacing-xspacing/4, a_y+yspacing-yspacing/4, fill = "green")
				# 	self.temp_GA[(x, y)] = (a_x + xspacing / 2, a_y + yspacing / 2)
				a_y += yspacing

			a_y = 2
			a_x += xspacing

	def draw_path(self):
		u''''''
		xspacing = self.cwidth / self.wide
		yspacing = self.cheight / self.high
		a_x = 2
		a_y = 2
		self.temp_GA = {}
		self.new_maze_path = self.GA_path()
		for x, i in enumerate(self.maze):
			for y, i1 in enumerate(i):
				if (x, y) in self.new_maze_path:
					# self.canvas.create_oval(a_x+(xspacing/4), a_y+(yspacing/4), a_x+xspacing-xspacing/4, a_y+yspacing-yspacing/4, fill = "green")
					self.temp_GA[(x, y)] = (a_x + xspacing / 2, a_y + yspacing / 2)
				a_y += yspacing
			a_y = 2
			a_x += xspacing

		# for i, s in enumerate(self.new_maze_path[:-1]):
		# 	self.canvas.create_line(self.temp_GA[s][0], self.temp_GA[s][1], self.temp_GA[self.new_maze_path[i + 1]][0],
		# 							self.temp_GA[self.new_maze_path[i + 1]][1], fill="green")
        #
		# print(self.new_maze_path)
		# print(len(self.new_maze_path))

		for i, s in enumerate(self.new_maze_path[:-1]):

			u'''draw maze path'''

			self.canvas.create_line(self.temp_GA[s][0], self.temp_GA[s][1], self.temp_GA[self.new_maze_path[i + 1]][0],
									self.temp_GA[self.new_maze_path[i + 1]][1], fill="red", dash=(4, 4))
			self.root.update_idletasks()
			self.root.update()

			time.sleep(0.001)

	def draw_pop_path1(self, path, ball_color, path_max_length):

		xspacing = self.cwidth / self.wide
		yspacing = self.cheight / self.high
		temp_path = {}
		total_temp = []
		id = []

		for count in range(len(path)):
			a_x = xspacing / 2
			a_y = yspacing / 2
			temp_path[0, 0] = (a_x, a_y)

			for i in range(len(path[count]))[1:]:
				deltaX = path[count][i][0] - path[count][i - 1][0]
				deltaY = path[count][i][1] - path[count][i - 1][1]
				temp_path[(path[count][i][0], path[count][i][1])] = (
				a_x + (xspacing) * deltaX, a_y + (yspacing) * deltaY)
				a_x, a_y = temp_path[(path[count][i][0], path[count][i][1])]

			total_temp.append(temp_path)
			if ball_color % 2 == 0:
				haha = self.canvas.create_oval(10, 10, 25, 25, fill="red")
			elif ball_color % 2 == 1:
				haha = self.canvas.create_oval(10, 10, 25, 25, fill="blue")
			id.append(haha)

			u'''define the location of ball'''
			self.canvas.move(id[count], random.uniform(0, xspacing / 3),random.uniform(0, yspacing / 3))

		for i in range(path_max_length):
			passby = 0
			for count in range(len(path)):
				temp_path = total_temp[count]
				x = path[count]
				if i < len(x) - 1:
					passby = 1
					heng = temp_path[x[i + 1][0], x[i + 1][1]][0] - temp_path[x[i][0], x[i][1]][0]
					shu = temp_path[x[i + 1][0], x[i + 1][1]][1] - temp_path[x[i][0], x[i][1]][1]
					self.canvas.move(id[count], heng, shu)

			if passby == 1:
				self.root.update_idletasks()
				self.root.update()
				time.sleep(0.001)

	def reach_next_grid(self, current, direction):

		if direction == [0, 0] and self.maze[current[0]][current[1]].up == True:
			new_grid = (current[0], current[1] - 1)

		elif direction == [0, 1] and self.maze[current[0]][current[1]].down == True:
			new_grid = (current[0], current[1] + 1)

		elif direction == [1, 0] and self.maze[current[0]][current[1]].left == True and current != (0, 0):
			new_grid = (current[0] - 1, current[1])

		elif direction == [1, 1] and self.maze[current[0]][current[1]].right == True:
			new_grid = (current[0] + 1, current[1])

		else:
			new_grid = current

		return new_grid


	def GA_path(self):
		pop_size = 1000	# poptlation size
		chrom_length = 4 * self.wide * self.high	# chromosome length
		# chrom_length = (self.wide + self.high) * (self.wide + self.high)
		pop = geneEncoding(pop_size, chrom_length)

		x = 0
		exit_flag = False

		while True:
			path = []

			for i in range(pop_size):
				current = (0, 0)
				temp = [(0, 0)]

				for j in range(chrom_length):
					if len(temp) == 1 and current != temp[-1]:
						temp.append(current)
					if len(temp) >= 2 and current != temp[-2] and current != temp[-1]:
						temp.append(current)

					new_grid = self.reach_next_grid(temp[-1], pop[i][j])
					current = new_grid

					if current == (self.wide - 1, self.high - 1):
						temp.append(current)
						exit_flag = True
						break
				path.append(temp)

			for i in range(len(path)):
				count = 0
				obj_value = path[i][-1]

				if self.maze[obj_value[0]][obj_value[1]].up == False:
					count += 1
				if self.maze[obj_value[0]][obj_value[1]].down == False:
					count += 1
				if self.maze[obj_value[0]][obj_value[1]].left == False:
					count += 1
				if self.maze[obj_value[0]][obj_value[1]].right == False:
					count += 1

				if count >= 3:
					pop[i] = []
					for j in range(chrom_length):
						temp = []
						temp.append(random.randint(0, 1))
						temp.append(random.randint(0, 1))
						pop[i].append(temp)

			fit_value, avg_value = calValue(path, self.wide, self.high)  # calculate fitness value
			best_fit, best_individual, best_path = best(pop, fit_value, path)  # find the best fitness value, the best individual and the best path
			cumulative_prob = selection(fit_value)  # calculate cumulative probability
			pop = crossover(pop, cumulative_prob, fit_value, best_fit, avg_value)  # crossover

			pm = cal_pm(fit_value, best_fit, avg_value)	# calculate mutation rate
			pop = mutation(pop, pm)  # mutation

			fit_temp = numpy.sort(fit_value)
			path_draw = []
			count_temp = 0
			for count in range(len(path)):
				if fit_value[count] >= fit_temp[-3]:
					path_draw.append(path[count])
					count_temp += 1
			self.draw_pop_path1(path_draw, x, self.wide * self.high)

			print('*******************************')
			print('Iteration: ' + str(x))
			print('*******************************')

			# if exit_flag:
			if exit_flag or x == 1000:
				break

			x += 1

		return best_path

if __name__ == "__main__":
	m = generate_maze()
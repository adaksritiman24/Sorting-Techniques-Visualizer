import turtle as tl
import time
import numpy as np
import random

# This is a visualization of different sorting techniques that I have learnt.
# The set of bars represent the array and the height of each bar represents the magnitude of the element in the array at that index position.
# I have used turtle graphics to make the visualization and the user interface.

# Time complexities:
# 	heap sort --> O(n log n)
# 	merge sort ---> O(n log n)
# 	quick sort ---> O(n log n)
# 	bubble sort ---> O(n^2)
# 	insertion sort --->O(n^2)


class Heap:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.arr = np.array(self.arr)
	def heapify(self, temp):
		self.temp = temp
		for i in range(self.len):
			m = i
			while True:
				if self.arr[m]>=self.arr[m//2]:
					temp = self.arr[m]
					self.arr[m] = self.arr[m//2]
					self.arr[m//2] = temp
				if m==0:
					break	
				m=m//2
		self.temp.move_height(list(self.arr))	
	def reheap(self, index):
		for i in range(index+1):
			m = i
			while True:
				if self.arr[m]>=self.arr[m//2]:
					temp = self.arr[m]
					self.arr[m] = self.arr[m//2]
					self.arr[m//2] = temp
				if m==0:
					break	
				m=m//2
		for i in range(index+2):		
			self.temp.ts[i].color("white")
			time.sleep(0.01)
			self.temp.ts[i].color("red")		
		self.temp.move_height(list(self.arr))				
	def sort(self):
		for i in range(self.len-1,-1, -1):
			 temp =self.arr[0] 	
			 self.arr[0] = self.arr[i]
			 self.arr[i] = temp
			 self.reheap(i-1)



class Insertion:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.arr = np.array(self.arr)
	def sort(self, temp):
		self.temp = temp
		for i in range(1,self.len):
			temporary = self.arr[i]
			for j in range(i-1,-1,-1):
				self.temp.ts[j].color("green")
				time.sleep(0.05)
				self.temp.ts[j].color("red")
				if temporary< self.arr[j]:
					self.arr[j+1] = self.arr[j]
				else:
					self.arr[j+1]= temporary	
					break
				if j==0:
					self.arr[j] = temporary
					break
			try:			
				self.temp.ts[i+1].color("yellow")
				self.temp.move_height(list(self.arr))
				self.temp.ts[i+1].color("red")	
			except:						
				self.temp.move_height(list(self.arr))

class Quick:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.arr = np.array(self.arr)
	def start(self, temp):
		self.temp = temp
		self.quick(0,self.len -1)
	def quick(self, lo, hi):
		if hi>lo:
			pivot =	self.sort(lo, hi)
			self.quick(lo,pivot -1)
			self.quick(pivot+1, hi)
	def	sort(self, lo, hi):
		pivot = self.arr[hi]
		i= lo-1
		self.temp.ts[hi].color("yellow")
		for j in range(lo,hi):
			self.temp.ts[j].color("green")	
			time.sleep(0.03)
			self.temp.ts[j].color("red")
			if self.arr[j]<pivot:
				i+=1
				temporary = self.arr[i]
				self.arr[i] = self.arr[j]
				self.arr[j] = temporary


		temporary = self.arr[i+1]
		self.arr[i+1] = self.arr[hi]
		self.arr[hi] = temporary
		time.sleep(0.3)
		self.temp.ts[hi].color("red")	
		self.temp.ts[i+1].color("yellow")	
		self.temp.move_height(list(self.arr))
		

		time.sleep(0.3)
		self.temp.ts[i+1].color("red")
		return i+1 		


class Merge:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.arr =np.array(self.arr)
	def start(self, temp):
		self.temp = temp	
		self.merge(0, self.len-1)
	def merge(self,lo,hi):
		if hi>lo:
			mid = lo + (hi-lo)//2
			self.merge(lo, mid)
			self.merge(mid+1, hi)
			self.sort(lo, mid, hi)
	def sort(self, lo, mid,hi):
		ol = lo
		ul = hi
		start =lo
		i = mid-lo+1
		j = hi - mid
		left = np.zeros(i)
		right = np.zeros(j)
		for x in range(i):
			left[x] = self.arr[lo]
			lo+=1
		for y in range(j):
			right[y] = self.arr[mid+1]
			mid+=1	
		x=0
		y=0	
		while x<i and y<j:
			if left[x]<right[y]:
				self.arr[start]	= left[x]
				x+=1
				start+=1
			else:
				self.arr[start] = right[y]
				y+=1
				start+=1
		while x<i:
			self.arr[start]=left[x]
			start+=1
			x+=1

		while y<j:
			self.arr[start]=right[y]

			start+=1
			y+=1
		for i in range(ol, ul+1):	
			self.temp.ts[i].color("yellow")
			time.sleep(0.02)
			self.temp.ts[i].color("red")	
		self.temp.move_height(list(self.arr))


# l=[]
# for i in range(20):
# 	l.append(random.randint(2,25))
# print(l)	
# y = Merge(l)
# print(y.arr)

class Bubble:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.arr =np.array(self.arr)
	def sort(self, temp):
		self.temp = temp
		for i in range(self.len):
			for j in range(0,self.len-1-i):
				self.temp.ts[j].color("yellow")
				self.temp.ts[j+1].color("green")
				if self.arr[j]>self.arr[j+1]:
					temporary= self.arr[j]
					self.arr[j] = self.arr[j+1]
					self.arr[j+1] = temporary
				self.temp.ts[j].color("red")
				self.temp.ts[j+1].color("red")
			self.temp.move_height(list(self.arr))	


class Template():
	def __init__(self):
		self.height = 700
		self.width = 1000
		self.bars = np.linspace(-460,460,30)
		self.draw()

	def draw(self):	
		self.scr = tl.Screen()	
		self.scr.setup(self.width, self.height)
		self.scr.title("Sorting Techniques Visualization")
		self.scr.bgcolor("gray")
		self.bg = tl.Turtle()
		self.bg.shape("square")
		self.bg.shapesize(23,48)
		self.bg.goto(0,-85)
		self.write()
		self.draw_height()
		self.listen()
		self.scr.mainloop()


	def bubble_sort(self):
		self.y = Bubble(self.list)
		self.y.sort(self)

	def merge_sort(self):
		self.y = Merge(self.list)
		self.y.start(self)	

	def quick_sort(self):
		self.y = Quick(self.list)
		self.y.start(self)	

	def insertion_sort(self):
		self.y = Insertion(self.list)
		self.y.sort(self)	

	def heap_sort(self):
		self.y = Heap(self.list)
		self.y.heapify(self)
		self.y.sort()					

	def draw_height(self):
		self.list = []
		self.ts = []
		for i in range(30):
			self.h = random.randint(2, 100)
			self.list.append(self.h)
			self.t = tl.Turtle()
			self.t.penup()
			self.t.speed(0)
			self.t.shape("square")
			self.t.color("red")
			self.t.shapesize(self.h/5, 1)
			self.t.setx(self.bars[i])
			self.t.sety(-310 + (self.h/5)*10)
			self.ts.append(self.t)
	def randomise(self):
		l = []
		for i in range(30):
			self.h = random.randint(2, 100)
			l.append(self.h)
		self.move_height(l)	
				
	def move_height(self, l):
		for i in range(len(l)):
			self.ts[i].shapesize(l[i]/5, 1)
			self.ts[i].sety(-310 + (l[i]/5)*10)
			self.list= l

	def listen(self):
		self.scr.onkeypress(self.merge_sort, "m")
		self.scr.onkeypress(self.bubble_sort,"b")
		self.scr.onkeypress(self.quick_sort,"q")
		self.scr.onkeypress(self.insertion_sort,"i")
		self.scr.onkeypress(self.heap_sort,"h")
		self.scr.onkeypress(self.randomise,"r")
		self.scr.listen()	

	def write(self):
		self.pen = tl.Turtle()
		self.pen.penup()
		self.pen.hideturtle()
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.goto(-480,300)
		self.pen.write("Sorting Visualizations",False,align="left",font=("arial",20,"bold"))	
		self.pen.goto(-480,270)
		self.pen.write("Instructions:",False,align="left",font=("arial",15,"bold"))	
		self.pen.goto(-480,250)
		self.pen.write("a) Press 'r' in the keyboard to randomize array",False,align="left",font=("arial",10,"bold"))	
		self.pen.goto(-480,230)
		self.pen.write("b) Press 'b' in the keyboard for bubble sort",False,align="left",font=("arial",10,"bold"))	
		self.pen.goto(-480,210)
		self.pen.write("c) Press 'i' in the keyboard for insertion sort",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,190)
		self.pen.write("d) Press 'q' in the keyboard for quick sort",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,170)
		self.pen.write("e) Press 'm' in the keyboard for merge sort",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,150)
		self.pen.write("f) Press 'h' in the keyboard for heap sort",False,align="left",font=("arial",10,"bold"))				


if __name__ == "__main__":
	Template()
from sys import stdin
from collections import deque,Counter,defaultdict
import sys
import math,os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import time
import random

class Snake:
    class player_class:
        def __init__(self,x,y):
            self.x = x
            self.y = y

    def __init__(self,row,col,player):
        self.row = row
        self.col = col
        self.player = 0
        self.size = player
        self.dice = None
        self.player_obj = []

        for i in range(self.size):
            self.player_obj.append(self.player_class(self.row-1,0))

        self.pos = [self.row-1,0]
        self.player_name = {0:'First',1:'Second',2:'Third',3:'Fourth'}
        self.grid = [[' * ' for j in range(self.col)] for i in range(self.row)]
        self.grid[0][0] = ' E '
        for i in range(self.size):
            self.grid[self.player_obj[i].x][self.player_obj[i].y] = ' '+str(i)+' '

    def find(self,k):
        self.char = ' '+str(k+1)+' '

    def make_grid(self): # makes the grid array
        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.size):
                    if j!=self.player_obj[k].y or i!=self.player_obj[k].x:
                        self.grid[i][j] = ' * '
                    self.grid[self.player_obj[k].x][self.player_obj[k].y] = ' '+\
                    str(k+1)+ ' '

    def turn(self): #increase player turn by 1
        self.player = (self.player+1)%self.size

    def roll_dice(self): # rolls the dice
        a = [1,2,3,4,5,6]
        for i in range(30):
            self.dice = a[i%6]
            os.system('clear')
            self.display_grid()
        self.dice = random.randint(1,6)

    def display_grid(self): # to make the grid
        self.make_grid()
        for i in range(self.row):
            for j in range(self.col):
                print(self.grid[i][j],end = '')
            print()
        print("Dice: {} | Turn: {} | Exit: x".format(self.dice,self.player_name[self.player]))

    def move(self): # move the player
        temp = self.dice
        while temp:
            if self.player_obj[self.player].x % 2 == 1:
                op = operator.add
            else:
                op = operator.sub
            self.player_obj[self.player].y = op(self.player_obj[self.player].y,1)

            if  self.player_obj[self.player].y > self.col-1:
                self.player_obj[self.player].x -= 1
                self.player_obj[self.player].y = self.col-1

                self.grid[self.player_obj[self.player].x][self.player_obj[self.player].y] = ' '+\
                str(self.player) + ' '

            if  self.player_obj[self.player].y < 0:
                self.player_obj[self.player].x -= 1
                self.player_obj[self.player].y = 0

                self.grid[self.player_obj[self.player].x][self.player_obj[self.player].y] = ' '+\
                str(self.player) + ' '

            os.system('clear')
            self.display_grid()
            time.sleep(0.2)
            temp-=1


print("Enter number of players (MAX 4)")
p = int(input())
print("Enter the grid size NxN")
size = int(input())
obj = Snake(size,size,p)
os.system('clear')
obj.display_grid()
while (n:=input())!='x':
    if n == 'r' or n == 'R':
        obj.roll_dice()
        obj.turn()
        obj.move()
    os.system('clear')
    obj.display_grid()


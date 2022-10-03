import pygame
import random
import time
import math
class sorting:
    def __init__(self):
        self.x,self.y = 1920,1080
        self.sorted = (123,199,50)
        self.unsorted = (152,30,30)
        self.runn = (30,30,30)
        self.background = (228,191,156)
        self.start_x = 450
        self.font_loc = "/home/mukul/Downloads/OpenSans-Regular.ttf"

    def button(self):
        print("1. Insertion Sort")
        print("2. Selection Sort")
        print("3. Merge Sort")
        print("4. Quick Sort")
        print("1. Bubble Sort")

    def info(self,screen,x,y,name):
        self.textcolor = (50,50,50)
        pygame.draw.rect(screen,self.background,(x,y,x+125,y+240))
        fontObj = \
            pygame.font.Font(self.font_loc,18)
        val1 = fontObj.render('KEYS:',True,self.textcolor)
        val2 = fontObj.render('1.Insertion-Sort: i/I',True,self.textcolor)
        val3 = fontObj.render('2.Merge-Sort: m/M',True,self.textcolor)
        val4 = fontObj.render('3.Selection-Sort: s/S',True,self.textcolor)
        val5 = fontObj.render('4.Bubble-Sort: b/B',True,self.textcolor)
        val6 = fontObj.render('5.Quick-Sort: q/Q',True,self.textcolor)
        val7 = fontObj.render('6.Reset: r/R',True,self.textcolor)
        val9 = fontObj.render('SORTED',True,self.textcolor)
        val10 = fontObj.render('UNSORTED',True,self.textcolor)
        val11 = fontObj.render('IN-PROGRESS',True,self.textcolor)
        val12 = fontObj.render('ALGORITHM: '+str(name),True,self.textcolor)

        screen.blit(val1,(x,y))
        screen.blit(val2,(x,y+20))
        screen.blit(val3,(x,y+40))
        screen.blit(val4,(x,y+60))
        screen.blit(val5,(x,y+80))
        screen.blit(val6,(x,y+100))
        screen.blit(val7,(x,y+120))
        screen.blit(val12,(x,y+280))

        pygame.draw.rect(screen,(0,255,0),(x,y+190,50,30))
        screen.blit(val9,(x+60,y+190))

        pygame.draw.rect(screen,(255,0,0),(x,y+220,50,30))
        screen.blit(val10,(x+60,y+220))

        pygame.draw.rect(screen,(30,30,30),(x,y+250,50,30))
        screen.blit(val11,(x+60,y+250))



    def bar(self,screen,x,y,color,height,width):
        font = pygame.font.Font(self.font_loc,20)
        pygame.draw.rect(screen,color,(x,y-8*height,width,8*height))
        txt = font.render(str(height),True,(20,20,20))
        screen.blit(txt,(x,y-8*height-40))

    def make(self,arr,screen,i,j,ele,name):
        self.info(screen,50,50,name)
        pygame.draw.rect(screen,(30,30,30),(self.start_x-30,930,1000,12))
        if name == 'bubble':
            x = self.start_x
            for r in range(len(arr)):
                if r == j+1 or r==j:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                elif r >= len(arr)-i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'insertion':
            x = self.start_x
            for r in range(len(arr)):
                if r == j:
                    self.bar(screen,x,930,self.runn,ele,20)
                elif r<=i-1:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'array':
            x = self.start_x
            for i in range(len(arr)):
                self.bar(screen,x,930,ele,arr[i],20)
                x+=30
        elif name == 'merge':
            x = self.start_x
            for r in range(len(arr)):
                if r <= i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                elif r>=j:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'selection':
            x = self.start_x
            for r in range(len(arr)):
                if r == j or r == i:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                elif r<i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'quicksort':
            x = self.start_x
            for r in range(len(arr)):
                if r == ele:
                    self.bar(screen,x,930,(122,122,122),arr[ele],20)
                elif r == j or r == i:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                elif r<i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                elif r>i:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30

    def bubblesort(self,arr,screen,speed):
        for i in range(len(arr)):
            for j in range(len(arr)-1-i):
                screen.fill((self.background))
                self.make(arr,screen,i,j,None,'bubble')
                clock.tick(speed)
                pygame.display.update()
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    screen.fill((self.background))
                    self.make(arr,screen,i,j,None,'bubble')
                    clock.tick(speed)
                    pygame.display.update()

    def selectionsort(self,arr,screen,speed):
        for i in range(0,len(arr)):
            minElement = arr[i]
            index = i
            for j in range(i+1,len(arr)):
                if arr[j]<minElement:
                    minElement=arr[j]
                    index=j
            screen.fill((self.background))
            self.make(arr,screen,i,index,None,'selection')
            clock.tick(speed)
            pygame.display.update()
            arr[i],arr[index] = arr[index],arr[i]
        return arr

    def cleanarray(self,arr,screen,color):
        screen.fill(self.background)
        sort.make(arr,screen,None,None,color,'array')
        pygame.display.update()

    def insertionsort(self,arr,screen,speed):
        for i in range(1,len(arr)):
            ele = arr[i]
            j = i
            while j>0 and arr[j-1]>ele:
                arr[j] = arr[j-1]
                screen.fill((self.background))
                self.make(arr,screen,i,j,ele,'insertion')
                j-=1
                clock.tick(speed)
                pygame.display.update()
            screen.fill((self.background))
            arr[j] = ele
            self.make(arr,screen,i,j,ele,'insertion')
            clock.tick(speed)
            pygame.display.update()


    def quicksort(self,arr,screen,speed,a,b):
        if a>=b:
            return
        pivot = arr[b]
        left = a
        right = b-1
        while left<=right:
            while left<=right and arr[left]<pivot:
                left+=1
            while left<=right and arr[right]>pivot:
                right-=1
            if left<=right:
                arr[left],arr[right] = arr[right],arr[left]
                left,right = left+1,right-1

                screen.fill((self.background))
                self.make(arr,screen,left,right,b,'quicksort')
                clock.tick(speed)
                pygame.display.update()

        arr[left],arr[b] = arr[b],arr[left]

        screen.fill((self.background))
        self.make(arr,screen,left,b,b,'quicksort')
        clock.tick(speed)
        pygame.display.update()

        self.quicksort(arr,screen,speed,a,left-1)
        self.quicksort(arr,screen,speed,left+1,b)



    def mergesort(self,s1,s2):
        i,j = 0,0
        ct = [0]*(len(s1)+len(s2))
        while i+j<len(ct):
            if j == len(s2) or (i<len(s1) and s1[i]<s2[j]):
                ct[i+j] = s1[i]
                i+=1
            else:
                ct[i+j] = s2[j]
                j+=1
        return ct

    def merge(self,arr,screen,speed):
        l = len(arr)
        step = 2
        for i in range(int(math.log2(l))):
            ax = []
            n = 0
            while n<l:
                nums = arr[n:n+step]
                length = len(nums)
                nums = self.mergesort(nums[0:length//2],nums[length//2:])

                screen.fill((self.background))
                self.make(arr,screen,n,n+step+1,len(arr),'merge')
                clock.tick(speed+5)
                pygame.display.update()

                for x in nums:
                    ax.append(x)
                n+=step
            arr = ax

            screen.fill((self.background))
            self.make(arr,screen,n,n+step+1,0,'merge')
            clock.tick(speed)
            pygame.display.update()

            step*=2
        return arr


pygame.init()
sort = sorting()
screen = pygame.display.set_mode((sort.x,sort.y))
screen.fill((sort.background))
clock = pygame.time.Clock()
run = True
arr = [random.randint(1,90) for i in range(32)]
sort.cleanarray(arr,screen,sort.unsorted)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if sorted(arr)==arr:
                arr = [random.randint(1,90) for i in range(32)]
            if event.key == pygame.K_q:
                sort.quicksort(arr,screen,5,0,len(arr)-1)
            elif event.key == pygame.K_b:
                sort.bubblesort(arr,screen,45)
            elif event.key == pygame.K_i:
                sort.insertionsort(arr,screen,20)
            elif event.key == pygame.K_s:
                sort.selectionsort(arr,screen,5)
            elif event.key == pygame.K_m:
                sort.merge(arr,screen,1)
            elif event.key == pygame.K_r:
                arr = [random.randint(1,90) for i in range(32)]
                sort.cleanarray(arr,screen,(sort.unsorted))

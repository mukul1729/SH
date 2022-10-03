a = input("Enter a string with 4 or as many words as u want \n")
x = -1
for i in range(len(a)):
    if a[i] == ' ' or i==len(a)-1:
        for j in range(i,x,-1):
            print(a[j],end='')
        print(' ',end='')
        x = i

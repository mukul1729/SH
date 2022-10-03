import sys
def sum_number(num):
    s=0
    while num!=0:
        mod=num%10
        num=num//10
        s=s+pow(mod,2)
    temp=s
    if s==1:
        print("True")
        sys.exit()
    sum_number(temp)
print(sum_number(19))

Output:
True

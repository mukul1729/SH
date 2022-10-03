def find_it(seq):
    p=0
    for x in seq:
        for index in range(0,len(seq)):
            if x == seq[index]:
                p+=1
        if p%2!=0:
            return x
            exit()
        else:
            p=0
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,-1]))


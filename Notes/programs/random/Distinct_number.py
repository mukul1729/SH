a = [1,2,3]
x = 1
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if j == i:
            continue
        if a[i]==a[j]:
            x = 0
if x == 0:
    print("Not Distinct")
else:
    print("Distinct")

            

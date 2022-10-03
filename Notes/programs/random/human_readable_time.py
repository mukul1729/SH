def make_readable(seconds):
    d = {}
    time = ""
    i = {1:3600,2:60,3:1}
    for x in i.keys():
            d[x] = seconds//int(i[x])
            seconds = seconds % int(i[x])
            if d[x]<10:
                time = time + "0" + str(d[x]) + ":"
            else:
                time = time + str(d[x]) + ":"
            print(d)
    return ''.join(str(time[i]) for i in range(0,len(time)-1))
print(make_readable(7000))

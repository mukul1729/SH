def sum_pairs(ints, s):
    pair=[]
    result=[]
    for i in range(0,len(ints)):
        for j in range(0,len(ints)):
            if ints[i] + ints[j] == s:
                pair.append(ints[i])
                pair.append(ints[j])
    result.append(min(pair))
    result.append(max(pair))
    return result
print(sum_pairs([1,2,4,3,6,5],7))

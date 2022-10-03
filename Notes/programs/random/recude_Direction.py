def dirReduc(arr):
    d1 = {"NORTH":"SOUTH","SOUTH":"NORTH","WEST":"EAST","EAST":"WEST"}
    ans = []
    for a in range(len(arr)):
        if len(ans)>0:
            if d1[ans[-1]] == arr[a]:
                ans.pop()
                continue
        if arr[a] in d1.keys():
            ans.append(arr[a])
    return ans
        
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

def done_or_not(board): #board[i][j]
  s=0
  arr=[]
  for a in range(9):
    p=len(set(board[a]))
    s+=p
  p=0
  for a in range(9):
    for j in range(9):
        arr.append(board[j][a])
    p=len(set(arr))
    s+=p
    del arr[0:9]
  if s==162:
    return 'Finished!'
  else:
    return 'Try again!'
 
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

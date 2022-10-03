class Solution:
    def productExceptSelf(self,nums):
        mul=1
        left=[]
        right=[]
        left.append(1)
        for i in range(1,len(nums)):
            mul=nums[i-1]*mul 
            left.append(mul)
        nums=nums[len(nums)::-1]
        mul=1
        for i in range(1,len(nums)):
            mul=nums[i-1]*mul
            right.append(mul)
        right=right[::-1]
        right.append(1)
        mul=1
        for a in range(len(nums)):
            nums[a]=right[a]*left[a]
        return nums
a=Solution()
print(a.productExceptSelf([1,2,3,4]))

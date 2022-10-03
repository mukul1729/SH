class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxi = A[0]
        curr = 0
        for i in A:
            curr += i
            if curr<0:
                curr = 0
            maxi = max(maxi,curr)
        return maxi


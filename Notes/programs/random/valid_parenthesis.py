class Solution:
    def isValid(self,s):
        a=[]
        d={')':'(',']':'[','}':'{'}
        for i in range(0,len(s)):
            if s[i]=='[' or s[i]=='(' or s[i]=='{':
                a.append(s[i])
            
            if s[i]==']' or s[i]=='}' or s[i]==')':
                if len(a)==0:
                    return False
                if a[-1]==d[s[i]]:
                    a.pop()
                else:
                    return False

        return a==[]
p=Solution()
print(p.isValid('(){}'))


class Solution:
    def romanToInt(self,s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s1=0
        for i in range(len(s)):
            if i<len(s)-1:
                if d[s[i+1]]>d[s[i]]:
                    s1=s1-d[s[i]]
                else:
                    s1 = s1+d[s[i]]
            else:
                s1=s1+d[s[i]]
        return s1
a=Solution()
print(a.romanToInt('MCMXCIV'))

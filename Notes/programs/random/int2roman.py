class Solution():
    def intToRoman(self,num):
        d={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        ans=""
        sub=num
        while num!=0:
            for i in d.keys():
                if sub>num-i and num-i>=0:
                    a=i               
                sub=num-i
            ans=ans+str((d[a])) 
            num=num-a
            sub=num
        return ans
x=Solution()
print(x.intToRoman(1994))

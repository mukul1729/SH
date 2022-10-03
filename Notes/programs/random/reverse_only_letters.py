class Solution:
    def reverseOnlyLetters(self,S):
        t=list(S)
        S=list(S)
        x=[]
        dash=[]
        for a in range(len(S)):
            if (ord(S[a])>=65 and ord(S[a])<=90) or (ord(S[a])>=97 and
                    ord(S[a])<=122):
                x.append(S[a])
            else:
                dash.append(a)
                continue
        S=x
        for a in range(len(S)//2):
            temp=S[a]
            S[a]=S[len(S)-1-a]
            S[len(S)-1-a]=temp
        ans="".join(S)
        i=0
        for a in range(len(t)):
            if (ord(t[a])>=65 and ord(t[a])<=90) or (ord(t[a])>=97 and
                    ord(t[a])<=122):
                t[a]=ans[i]
                i=i+1
            else:
                continue
        t="".join(t)
        return t
a=Solution()
print(a.reverseOnlyLetters("7_28]"))

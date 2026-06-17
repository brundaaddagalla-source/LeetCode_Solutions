class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(s):
            l=[]
            i=0
            while i<len(s):
                c=1
                while i+1<len(s) and s[i]==s[i+1]:
                    c+=1
                    i+=1
                else:
                    l.append([c,s[i]])
                    i+=1
            ns=""
            for i in l:
                w=""
                for j in i:
                    w+=str(j)
                ns+=w
            return ns
        
        s="1"
        for i in range(n-1):
            s=helper(s)
        return s
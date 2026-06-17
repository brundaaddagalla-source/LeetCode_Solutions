class Solution:
    def processStr(self, s: str, k: int) -> str:
        l=[]
        c=0
        for i in s:
            if i.isalpha():
                if i.islower():
                    c+=1
            elif i=="*":
                if c!=0:
                    c-=1
            elif i=="#":
                c=c*2
            elif i=="%":
                c=c
            l.append(c)
        if k>=c:
            return "."
        for i in range(len(s)-1,-1,-1):
            char=s[i]
            c=l[i]
            if char.isalpha():
                if char.islower():
                    p=c-1
                    if k==p:
                        return char
            elif char=="*":
                p=c+1
            elif char=="#":
                p=c//2
                k=k%p #we are not building a new string so we are trying to find the value from the initial given string only, so if the string is doubled, the original would be divided by 2, and then since the string is duplicated, we want to find the original index
                #duplicated: abcabc
                #original: abc
                #k=4, original=3
                #in duplicated at k=4 we have b, so to find it in original, we do k=k%original=k=4%3=1
                #original[1]=b
            elif char=="%":
                p=c
                k=c-1-k
                #like before, we are finding the value in the string before reversing
                #original, abcd
                #reversed: dcba
                #k=1, reversed=>c
                #in original 4-1-1=2, original[2]=c
        return "."

            

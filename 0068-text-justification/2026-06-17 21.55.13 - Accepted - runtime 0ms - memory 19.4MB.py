class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        r=[]
        l=[]
        le=0
        i=0
        while i<len(words):
            if le+len(l)+len(words[i])>maxWidth:
                #line complete case
                extra=maxWidth-le
                spaces=extra//max(len(l)-1,1)
                rem=extra%max(len(l)-1,1)
                for j in range(max(1,len(l)-1)):
                    l[j]+=" "*spaces
                    if rem:
                        l[j]+=" "
                        rem-=1
                r.append("".join(l))
                l=[]
                le=0
            l.append(words[i])
            le+=len(words[i])
            i+=1
        last=" ".join(l)
        trail=maxWidth-len(last)
        r.append(last+" "*trail)
        return r
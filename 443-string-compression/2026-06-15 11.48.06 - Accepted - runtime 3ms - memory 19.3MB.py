class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i=0
        while i<=len(chars)-1:
            c=1
            while i+1<len(chars) and chars[i]==chars[i+1]:
                i+=1
                c+=1
            
            s+=str(chars[i])
            if c>1:
                s+=str(c)
            i+=1
        chars[:]=list(s)
        return len(s)
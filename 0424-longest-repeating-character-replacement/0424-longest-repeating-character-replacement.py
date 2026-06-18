class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        left=0
        f=0
        r=0
        #this loop is for the right pointer
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1 #update the frequency of each letter as we go by
            f=max(f,d[s[i]]) #update the maximum frequency
            while (i-left+1)-f>k: #checking our condition if the letters that are needed to be updated exceed the give k value
            #if yes, then we move the left pointer ahead and reduce the frequency of that letter
                d[s[left]]-=1
                left+=1
            #keeping the size of the maximum length of the window which we found
            r=max(r, i-left+1) 
        return r

#https://www.youtube.com/watch?v=gqXU1UyA8pk
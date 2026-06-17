from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l=[]
        i=0
        while i<len(words)-1:
            if sorted(words[i])==sorted(words[i+1]):
                # l.append(words[i])
                words.pop(i+1)
            else:
                l.append(words[i])
                i+=1
        l.append(words[-1])
        return l
import re
import heapq
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph=paragraph.lower()
        words = re.split(r"[^a-z]+", paragraph)
        print(words)
        d={}
        for i in words:
            if i not in banned and i!="":
                d[i]=d.get(i,0)+1
        c=-1
        ans=""
        for i in d:
            if d[i]>c:
                c=d[i]
                ans=i
        return ans
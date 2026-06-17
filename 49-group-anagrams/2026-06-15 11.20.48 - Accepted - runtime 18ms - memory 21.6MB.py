class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            if d.get("".join(sorted(i)),0)==0:
                d["".join(sorted(i))]=[i]
            else:
                d["".join(sorted(i))].append(i)
        r=[]
        for i in d:
            r.append(d[i])
        return r
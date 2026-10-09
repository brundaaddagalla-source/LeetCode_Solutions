class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        r=0
        keys=sorted(list(d.keys()))
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                if keys[i]<keys[j]<target-(keys[i]+keys[j]) and target-(keys[i]+keys[j]) in keys:
                    r+= d[keys[i]]*d[keys[j]]*d[target-(keys[i]+keys[j])]
        for i in range(len(keys)):
            if keys[i]<target-keys[i]*2 and target-keys[i]*2 in keys:
                r+= d[keys[i]]*(d[keys[i]]-1)*d[target-keys[i]*2]//2
            if (target - keys[i]) % 2 == 0 and keys[i]<(target-keys[i])//2 and (target-keys[i])//2 in keys:
                r+= d[keys[i]]*(d[(target-keys[i])//2])* (d[(target-keys[i])//2]-1)//2
        for i in range(len(keys)):
            if target==keys[i]*3:
                    r+= d[keys[i]]*(d[keys[i]]-1)*(d[keys[i]]-2)//6
        return r % (10**9 + 7)
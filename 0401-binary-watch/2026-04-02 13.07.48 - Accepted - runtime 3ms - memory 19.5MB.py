class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        r=[]
        for i in range(12):
            for j in range(60):
                if bin(i).count("1")+bin(j).count("1")==turnedOn:
                    t=f"{i}:{j:02d}"
                    r.append(t)
        return r
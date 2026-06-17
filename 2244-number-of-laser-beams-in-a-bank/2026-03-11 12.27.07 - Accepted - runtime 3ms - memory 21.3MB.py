class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev=0
        beams=0
        for i in bank:
            x=i.count("1")
            if x>0:
                beams+=prev*x
                prev=x
        return beams
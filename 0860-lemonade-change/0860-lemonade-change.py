class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={}
        c=1
        for i in bills:
            d[i]=d.get(i,0)+1
            if i==10:
                if d.get(5,0)==0:
                    c=0
                    break
                else:
                    d[5]-=1
            if i==20:
                if d.get(10,0)==0:
                    if d.get(5,0)<=2:
                        c=0
                        break
                    else:
                        d[5]-=3
                else:
                    if d.get(5,0)<1:
                        c=0
                        break
                    else:
                        d[5]-=1
                        d[10]-=1            
        if c:
            return True
        else:
            return False
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #angle for 1 hr = 360/12=30
        #angle for 1 min= 360/60=6

        #total_hour=(hour+minute/60)*30
        #total_minu=(minute*6)
        #angle=total_hour-total_minu

        h=(hour+(minutes/60))*30
        m=minutes*6
        angle=abs(h-m)
        return angle if angle<=180 else 360-angle
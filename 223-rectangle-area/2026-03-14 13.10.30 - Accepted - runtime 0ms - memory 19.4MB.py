class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                          bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        x_left = max(ax1, bx1)
        y_bottom = max(ay1, by1)
        x_right = min(ax2, bx2)
        y_top = min(ay2, by2)
        a1 = (ax2 - ax1) * (ay2 - ay1)
        a2 = (bx2 - bx1) * (by2 - by1)
        if x_right > x_left and y_top > y_bottom:
            a3 = (x_right - x_left) * (y_top - y_bottom)
        else:
            a3 = 0
        return a1 + a2 - a3
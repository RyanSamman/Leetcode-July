import math


# https: // leetcode.com/problems/angle-between-hands-of-a-clock/
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = math.fabs(minutes*360/60 - (hour + minutes/60) * 360/12)
        if angle > 180:
            angle = 360 - angle
        return angle

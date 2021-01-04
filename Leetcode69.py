class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x/2 + 1
        while l <= r:
            m = (l + r) // 2
            if m > x / m:
                r = m - 1
            elif m < x / m:
                l = m + 1
            else:
                return int(m)
        return int(r)
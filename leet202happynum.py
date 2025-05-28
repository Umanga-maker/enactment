class Solution:
    def ishappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            sq_sum = 0
            while n > 0:
                sq_sum += (n%10) * (n%10)
                n = n // 10 #Floor division
            if sq_sum == 1:
                return True
            n = sq_sum
        return False
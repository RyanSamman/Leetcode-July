#https://leetcode.com/problems/powx-n/
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        # Timed out
        if n == 0:
            return 1

        flip = inverse = False
        if n % 2 != 0 and x < 0:
            x *= -1
            flip = True
        if n < 0:
            n *= -1
            inverse = True

        total = x

        for i in range(1, n):
            total *= x

        if flip:
            total *= -1
        if inverse:
            total = 1 / total

        return total

    def myPow(self, x: float, n: int) -> float:
        # Try #2
        if n == 0:
            return 1

        flip = inverse = False
        if n % 2 != 0 and x < 0:
            x *= -1
            flip = True
        if n < 0:
            n *= -1
            inverse = True
        hashtable = {1: x}
        total = x
        tpow = 1

        while tpow + tpow <= n:
            total = total * total
            tpow = tpow + tpow
            hashtable[tpow] = total

        remainingPower = n - tpow
        index = tpow
        while remainingPower > 0:
            if index > remainingPower or index not in hashtable:
                index //= 2
                continue

            total *= hashtable[index]
            remainingPower -= index

        if flip:
            total *= -1
        if inverse:
            total = 1 / total

        return total


if __name__ == '__main__':
    x = Solution()
    d = {"x": 2.1, "n": 3}
    print("answer 1", d['x'] ** d['n'])
    ans = x.myPow(**d)
    print("answer 2", ans)

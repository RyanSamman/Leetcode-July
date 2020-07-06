import math


class Solution:
	def alg(self, s):
		return s * (s + 1) / 2  # (s**2)/2 + s/2

	def arrangeCoins(self, n: int) -> int:
		left = 0
		right = 2000000

		prev1 = prev2 = prev3 = prev4 = 0

		while True:
			middle = (left + right) / 2
			solution = self.alg(middle)

			if n < solution:
				right = middle - 1
			else:
				left = middle + 1

			prev4 = prev3
			prev3 = prev2
			prev2 = prev1
			prev1 = middle

			if prev1 == prev3 and prev2 == prev4:
				break

		return int(middle)


test = Solution()
print(test.arrangeCoins(1804289383))

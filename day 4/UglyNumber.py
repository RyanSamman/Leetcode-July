# 1, 2, 5

# 1
# 2, 4, 8, 16, 32
# 6
# 3, 9, 27
# 15
# 5,

def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        L = arr[:m]
        R = arr[m:]

        mergeSort(L)
        mergeSort(R)

        print(L, R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        # print(num)
        while num % 2 == 0:
            num //= 2
            # print(num)

        while num % 3 == 0:
            num //= 3
            # print(num)

        while num % 5 == 0:
            num //= 5
            # print(num)

        return num == 1

    def nthUglyNumber(self, n: int) -> int:
        uglyArr = [1]
        i2 = i3 = i5 = 0

        for i in range(0, n - 1):
            two = 2 * uglyArr[i2]
            three = 3 * uglyArr[i3]
            five = 5 * uglyArr[i5]

            if two <= three and two <= five:
                i2 += 1

            if three <= two and three <= five:
                i3 += 1

            if five <= two and five <= two:
                i5 += 1

            uglyArr.append(min(two, three, five))

        print(uglyArr)
        return uglyArr[n - 1]


    def nthUglyNumber1(self, n: int) -> int:
        uglyArr = [None]
        i = 0
        j = 0
        while i < n:
            if self.isUgly(j):
                # print(j)
                uglyArr.append(j)
                i += 1
            j += 1
        print(uglyArr)
        return uglyArr[n]


x = Solution()

'''
for i in range(0, 30):
    if x.isUgly(i):
        print(i)
'''

print(x.nthUglyNumber(17))

'''
1
2
3
4
5
6
8
9
10
12
15
16
18
20
24
25
27
'''
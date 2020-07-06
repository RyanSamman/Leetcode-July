class Solution:
    def plusOne(self, digits):
        length = len(digits)
        print("testing", digits, length)
        i = length - 1

        while True:
            if i < 0:
                digits = [1] + digits
                break

            currentValue = digits[i]
            currentValue += 1

            if currentValue < 10:
                digits[i] = currentValue
                break

            digits[i] = 0
            i -= 1

        return digits


if __name__ == "__main__":
    test = Solution()
    print(test.plusOne([9, 9, 9, 9]))

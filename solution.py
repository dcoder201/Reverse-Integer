class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        # initialize the result number
        result = 0
        # extract digits from x and append them to the left of result
        while x > 0:
           digit = x % 10
           result = result * 10 + digit
           x //= 10
        # apply the sign to the result
        result *= sign
        # check if the result is within the range of a 32-bit signed integer
        if result < -2**31 or result > 2**31 - 1:
           return 0
        return result

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n // 2):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # ? ki total count odd hai
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference between fixed sums
        diff = left_sum - right_sum

        # Alice can force a win if the difference
        # cannot be balanced by the question marks
        return diff != (right_q - left_q) * 9 // 2
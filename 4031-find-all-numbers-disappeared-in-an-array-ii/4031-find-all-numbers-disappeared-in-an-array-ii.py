class Solution:

    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()

        ans = []
        start = lower

        for num in nums:

            if num < lower:
                continue

            if num > upper:
                break

            # Duplicate
            if num < start:
                continue

            # Missing range
            if num > start:
                ans.append([start, num - 1])

            start = num + 1

        # Remaining range
        if start <= upper:
            ans.append([start, upper])

        return ans
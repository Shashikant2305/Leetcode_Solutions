class Solution:

    def longestSubarray(self, nums: list[int], k: int) -> int:

        mx = max(nums)

        spf = list(range(mx + 1))

        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = []

            while x > 1:
                p = spf[x]
                factors.append(p)

                while x % p == 0:
                    x //= p

            return factors

        factors = [get_factors(x) for x in nums]

        count = {}
        distinct = 0
        left = 0
        ans = 0

        for right in range(len(nums)):

            for p in factors[right]:
                if count.get(p, 0) == 0:
                    distinct += 1

                count[p] = count.get(p, 0) + 1

            while distinct > k:

                for p in factors[left]:
                    count[p] -= 1

                    if count[p] == 0:
                        distinct -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans
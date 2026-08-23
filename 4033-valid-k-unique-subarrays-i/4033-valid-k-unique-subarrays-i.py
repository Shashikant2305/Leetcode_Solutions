class Solution:

    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:

        n = len(nums)
        q = len(queries)

      
        values = {x: i for i, x in enumerate(set(nums))}
        arr = [values[x] for x in nums]

        
        block = int(n ** 0.5)


        qs = []
        for i, (l, r) in enumerate(queries):
            qs.append((l, r, i))

        qs.sort(
            key=lambda x: (
                x[0] // block,
                x[1] if (x[0] // block) % 2 == 0 else -x[1]
            )
        )

        freq = [0] * len(values)

        distinct = 0
        odd_count = 0

        left = 0
        right = -1

        ans = [False] * q

        def add(x):
            nonlocal distinct, odd_count

            if freq[x] == 0:
                distinct += 1

            if freq[x] % 2 == 1:
                odd_count -= 1
            else:
                odd_count += 1

            freq[x] += 1

        def remove(x):
            nonlocal distinct, odd_count

            if freq[x] % 2 == 1:
                odd_count -= 1
            else:
                odd_count += 1

            freq[x] -= 1

            if freq[x] == 0:
                distinct -= 1

        for l, r, idx in qs:

            while right < r:
                right += 1
                add(arr[right])

            while right > r:
                remove(arr[right])
                right -= 1

            while left < l:
                remove(arr[left])
                left += 1

            while left > l:
                left -= 1
                add(arr[left])

            ans[idx] = (
                distinct == k
                and odd_count == 0
            )

        return ans
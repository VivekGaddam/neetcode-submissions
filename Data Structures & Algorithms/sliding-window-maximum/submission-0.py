import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []

        for i in range(k):
            heapq.heappush(h, (-nums[i], i))

        left = 0
        right = k - 1
        ans = []

        while True:
            while h and h[0][1] < left:
                heapq.heappop(h)

            x = -h[0][0]
            ans.append(x)

            right += 1
            left += 1

            if right >= len(nums):
                break

            heapq.heappush(h, (-nums[right], right))

        return ans
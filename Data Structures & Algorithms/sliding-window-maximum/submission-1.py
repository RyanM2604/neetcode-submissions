class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for r in range(len(nums)):
            # remove smaller elements from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # remove leftmost if out of window
            if q[0] < r - k + 1:
                q.popleft()

            # start adding results when window is full
            if r >= k - 1:
                res.append(nums[q[0]])

        return res
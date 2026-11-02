class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # store indices
        maxArea = 0
        heights.append(0)  # flush remaining stack

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea
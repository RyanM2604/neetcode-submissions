class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, idx]
        res = [0] * len(temperatures) # when theres possibility of all 0s or a default value, start by init the arr
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        
        return res

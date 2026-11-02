class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in lookup.keys():
                lookup[numbers[i]] = i
            else:
                return [lookup[target - numbers[i]] + 1, i + 1]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(numbers):
            complement = target - n

            if complement in dic:
                return [dic[complement] + 1, i + 1]
            dic[n] = i
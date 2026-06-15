class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        max_len = 1
        
        for i in range(n):
            for j in range(i + 1, n):
                valid = True
                for k in range(i, j):
                    if arr[k] == arr[k + 1]:
                        valid = False
                        break
                    if k > i:
                        if (arr[k - 1] < arr[k] and arr[k] > arr[k + 1]) or (
                            arr[k - 1] > arr[k] and arr[k] < arr[k + 1]):
                            continue
                        else:
                            valid = False
                            break
                if valid:
                    max_len = max(max_len, j - i + 1)
        return max_len
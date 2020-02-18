class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        num = arr.count(0)

        
        for i in range(len(arr) - 1, -1, -1):
            if i + num < len(arr):
                arr[num + i] = arr[i]
            if arr[i] == 0:
                num -= 1
                if i + num < len(arr):
                    arr[num + i] = 0
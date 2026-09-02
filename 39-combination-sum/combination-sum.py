class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, curr: List[int], summ: int):
            if summ == target:
                res.append(curr[:])
                return
            if summ > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, summ + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res
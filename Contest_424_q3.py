'''
https://leetcode.com/problems/zero-array-transformation-ii/
sweep line + binary search
time: O(nlog(n))
'''
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def helper(m):
            events = defaultdict(int)
            for i in range(m):
                l, r, v = queries[i]
                events[l] += v
                events[r+1] -= v
            diff = []
            curr = 0
            for i in range(len(nums)):
                if i in events:
                    curr += events[i]
                diff.append(curr)
            for i in range(len(nums)):
                if nums[i] - diff[i] > 0:
                    return False
            return True

        n = len(queries)
        l, r = 0, n
        found = False
        while l <= r:
            m = l + (r-l)//2
            if helper(m):
                found = True
                r = m - 1
            else:
                l = m + 1
        return l if found else -1
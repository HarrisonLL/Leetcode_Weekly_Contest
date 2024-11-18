'''
https://leetcode.com/problems/zero-array-transformation-i/

solution:
sweeping line.
the first element in query can be seemed as +1
the second element in query can be seemed as -1
in each index, find the net diff with original nums
time: O(n)
'''
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        m = len(queries)
        events = defaultdict(int)
        for i in range(m):
            l, r = queries[i]
            events[l] += 1
            events[r+1] -= 1
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
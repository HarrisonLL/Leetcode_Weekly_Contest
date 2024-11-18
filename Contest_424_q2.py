'''
https://leetcode.com/problems/zero-array-transformation-i/

solution:
sweeping line.
the first element in query can be seemed as +1
the second element in query can be seemed as -1
in each index, find the net diff with original nums
'''
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        events = defaultdict(int)
        for query in queries:
            events[query[0]] += 1
            events[query[1]+1] -= 1
        events = sorted(events.items())
        diff = []
        curr = 0
        for i in range(len(events)-1):
            curr += events[i][1]
            curr_idx = events[i][0]
            next_idx = events[i+1][0]
            while curr_idx < next_idx:
                diff.append(curr)
                curr_idx += 1
        diff.append(curr)
        for i in range(len(nums)):
            if nums[i] - diff[i] > 0:
                return False
        return True
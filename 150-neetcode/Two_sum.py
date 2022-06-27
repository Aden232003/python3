# https://leetcode.com/problems/two-sum/
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
nums = [2,7,11,15]
target1 = 9
store = {}
for i,n in enumerate(nums):
    dif = target1 - n
    if store[dif] in store:
        print(store[diff])
    else:
        store[dif] = i

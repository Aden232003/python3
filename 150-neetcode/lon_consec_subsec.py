#test cases
nums1 = [100,4,200,1,3,2] #output=4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
nums2 = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in numSet:
            length = 0
            while (length + n) in numSet:
                length+=1
            longest = max(length,longest)
    return longest

print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
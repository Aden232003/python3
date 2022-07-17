from cgi import test


class Solution:

    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue

            l,r = i+1 ,len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans


testA = [-1,0,1,2,-1,-4]
testB = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
sol = Solution()
print(sol.threeSum(testA))
print(sol.threeSum(testB))
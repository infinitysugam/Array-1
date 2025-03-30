#We calculate the left product and right product and then store it into an array and return that
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def productExceptSelf(self, nums):
        answer = [1 for i in  range(0,len(nums))]

        for i in range(0,len(nums)):
            if i == 0:
                answer[i] = 1
            else:
                answer[i] = nums[i-1]*answer[i-1]

        mul =  1

        for i in range(len(nums)-1,-1,-1):
            if i ==len(nums)-1:
                answer[i]=answer[i]*1
            else:
                answer[i] = answer[i]*nums[i+1]*mul
                mul = nums[i+1]*mul

        return answer

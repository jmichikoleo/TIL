# Leet Code Find the Duplicate Number Problem 

--- 

## Problem 

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. 
There is only one repeated number in `nums`, return this repeated number. 
You must solve the problem without modifying the array `nums` and using only constant extra space. 

---

## Progress Method 

- first we sort the numbers inside of the list
- next, we loop through each numbers on the list.
  - if the numbers are the same then we return the duplicate number.

---

## Code 

>
    def findDuplicate(self, nums: List[int]) -> int:
        # sort the list
        nums.sort()

        # loop through the numbers and find the same number
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

---

## Result 

- Test Case 1 : if the input is `[1,3,4,2,2]` then the output is `2`.
- Test Case 2 : if the input is `[3,1,3,4,2]` then the output is `3`.
- Test Case 3 : if the input is `[3,3,3,3,3]` then the output is `3`. 

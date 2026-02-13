# Leet Code Missing Number Problem 

---

## Problem 

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array. 

---

## Progress Method 

- first, we need to find the length of the number list.
- next, we need to find the expected sum and the actual sum of the number to find the missing number.
- after that, we find the missing number by subtracting the expected sum to the actual sum.

--- 

## Code 

>
    def missingNumber(self, nums: List[int]) -> int:
        # find the length of the number list
        n = len(nums)
        
        # find the expected sum and actual sum of the numbers 
        exp = n * (n + 1) // 2
        act = sum(nums)

        # return the missing number
        return exp - act

---

## Result 

- Test Case 1 : if the input is `[3,0,1]` then the output is `2`.
- Test Case 2 : if the input is `[0,1]` then the output is `2`.
- Test Case 3 : if the input is `[9,6,4,2,3,5,7,0,1]` then the output is `8`.


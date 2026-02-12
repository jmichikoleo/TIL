# Leet Code Combination Sum III Problem [260211] 

--- 

## Problem 

Find all valid combination of `k` numbers that sum up to `n` such that the following conditions are true : 

- Only numbers `1` through `9` are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order. 

--- 

## Progress Method 

- first we make a list of the numbers that's going to be used from 1 to 9.
- then we need create an empty list for the answer.
- after that we create a new function to check the current position in the list and also the current combination being built.
  - if the numbers adds up to n then we check if the length is the same as k, if the length are the same then we add it to the list.
  - after we reach the last number on the list, then we stop checking.
- now we use the check function to check the numbers on the list, starting by the first position then the next one and we start at 0 with an empty combination.
- lastly we return the answer.

---

## Code 

>
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        number = [1,2,3,4,5,6,7,8,9]
        answer = []

        def check(index, b): 
            if b and sum(b) == n: 
                if(len(b)) == k:
                    answer.append(b)
                return

            if (index >= len(number)):
                return

            check(index + 1, b + [number[index]])
            check(index + 1, b)
        
        check(0,[])
        return answer

---

## Result

- Test Case 1 : If the input is `k = 3` and `n = 7` then the output is `[[1,2,4]]`.
- Test Case 2 : If the input is `k = 3` and `n = 9` then the output is `[[1,2,6],[1,3,5],[2,3,4]]`.
- Test Case 3 : If the input is `k = 4` and `n = 1` then the output is `[]`.


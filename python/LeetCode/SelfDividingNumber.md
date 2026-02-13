# Leet Code Self Dividing Numbers Problem 

--- 

## Problem 

A self-dividing number is a number that is divisible by every digit it contains. 
- For example, `128` is a self-dividing number because `128 % 1 == 0`, `128 % 2 == 0`, and `128 % 8 == 0`.
A self-dividing number is not allowed to contain the digit zero.
Given two integers `left` and `right`, return a list of all the self-dividing numbers in the range `[left, right]` (both inclusive).

---

## Progress Method 

- first we make an empty list called answer.
- Next we loop throught the range of numbers from left to right.
- Next we convert the number i into a string and check each digit of i.
  - if the digit is 0 or if the remaining of the division is not equal to 0 then stop the loop.
  - otherwise, add the number to the answer list.
- lastly, we return the answer.

---

## Code 

>
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer =[]
        for i in range(left, right+1):
            for j in str(i):
                if int(j)==0 or i%int(j) !=0: 
                    break
            else:
                answer.append(i)
        
        return answer

---

## Result 

- Test Case 1 : if `left = 1` and `right = 22` then the output would be `[1,2,3,4,5,6,7,8,9,11,12,15,22]`.
- Test Case 2 : if `left = 47` and `right = 85` then the output would be `[48,55,66,77]`. 

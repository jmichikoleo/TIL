# Leet Code Fizz Buzz Problem [260211]

--- 

## Problem 

Given an integer `n`, return a string array `answer` (1-indexed) where : 
- `answer[i] == "FizzBuzz"` if i is divisible by 3 and 5.
- `answer[i] == "Fizz"` if i is divisible by 3.
- `answer[i] == "Buzz"` if i is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

--- 

## Progress Method 

- first we create an empty list called output.
- then we start a loop from 1 to n.
    - if the number can be divided by 15 then we want to add "FizzBuzz" to the list.
    - if the number can be divided by 3 then we want to add "Fizz" to the list.
    - if the number can be divided by 5 then we want to add "Buzz" to the list.
    - otherwise we want to convert the number into string and add it into the list.
- lastly, we return the output list.

--- 

## Code 
>
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range (1, n+1): 
            if i % 15 ==0:
                output.append("FizzBuzz")
            elif i % 3 ==0:
                output.append("Fizz")
            elif i % 5 ==0:
                output.append("Buzz")
            else:
                output.append(str(i))
                
        return output  

## Result 
- Test Case 1 : if `n = 3` then the output would be `["1", "2", "Fizz"]`
- Test Case 2 : if `n = 5` then the output would be `["1","2","Fizz","4","Buzz"]`
- Test Case 3 : if `n = 15` then the output would be `["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]`


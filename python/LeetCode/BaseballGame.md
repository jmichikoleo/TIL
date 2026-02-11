# Leet Code Baseball Game Problem [260211]

--- 

## Problem 
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record. 
You are given a list of strings `operations`, where `operations[i]` is the `ith` operation you must apply to the record and is one of the following: 

- an integer `x`.
  - record a new score of `x`. 
- `'+'` 
  - record a new score that is the sum of the previous two scores. 
- `'D'` 
  - record a new score that is the double of the previous score. 
- `'C'` 
  - invalidate the previous score, removing it from the record. 

Return the sum of all the scores on the record after applying all the operations. 
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid. 

---

## Progress Method 

- first we create an empty list called score. 
- next, we want to loop the string to check the characters inside of the operations list
  - if the character is "+" then we add a new score to the list in which the value is the sum of the previous two scores. 
  - if the character is "D" then we add a new score to the list in which the value is 2 multiplied by the previous score. 
  - if the character is "C" then we remove the previous score. 
  - otherwise if the input is a number, then we just add the number to the list as an integer. 
- lastly, we return the sum of the number in the list. 

--- 

## Code 

>
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for o in operations: 
            if o == "+":
                score.append(score[-1] + score[-2])
            elif o == "D":
                score.append(2 * score[-1])
            elif o == "C":
                score.pop()
            else:
                score.append(int(o))
        
        return sum(score)

## Result 
- Test Case 1 : if the input is `["5","2","C","D","+"]` then the output is `30`.
- Test Case 2 : if the input is `["5","-2","4","C","D","9","+","+"]` then the output is `27`.
- Test Case 3 : if the input is `["1","C"]` then the output is `0`. 

# Leet Code Kids with The Greatest Number of Candies Problem [260212]

---

## Problem 

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`,
denoting the number of extra candies that you have. 

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `ith` kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `false` otherwise. 

Note that multiple kids can have the greatest number of candies. 

--- 

## Progress Method

- first we want to find the maximum candies and put it inside of the m variable.
- next, we need to create a new empty list.
- after that we check for each kid's candies and use the if function :
  - if the candies that the kid has + the extra candies are more than or equal to maximum candies then append true.
  - otherwise append false.
- lastly, we return the nanswer.

--- 

## Code

>
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find maximum candies 
        m = max(candies)
        answer = []

        # Check each kid's candies 
        for c in candies:
            if c + extraCandies >= m:
                answer.append(True)
            else:
                answer.append(False)

        return answer

---

## Result

- Test Case 1 : if the input is `[2,3,5,1,3]` and the extra candies is `3` then the output is `[true,true,true,false,true]`.
- Test Case 2 : if the input is `[4,2,1,1,2]` and the extra candies is `1` then the output is `[true,false,false,false,false]`.
- Test Case 3 : if the input is `[12,1,12]` and the extra candies is `10` then the output is `[true,false,true]`.

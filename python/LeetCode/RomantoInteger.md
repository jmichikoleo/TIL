# Leet Code Roman to Integer Problem [260211]

---

## Problem 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

- I : 1
- V : 5
- X : 10
- L : 50
- C : 100
- D : 500
- M : 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

---

## Progress Method

- first we need to make a dictionary filled with the roman symbol and their value.
- then we create a variable (number) which starts at 0.
- next we want to replace a couple of things like the roman symbol for 4, 9, 40, 90, 400, and 900.
- after that, we're going to loop the char in the string(s) and check their value from the dictionary and add them.
- lastly, we want to return the total number value.

---

## Code 
>
    def romanToInt(self, s: str) -> int:

      num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += num[char]
        return number

## Results 
- Test Case 1 : if the input is `III` then the output would be `3`.
- Test Case 2 : if the input is `LVIII` then the output would be `58`.
- Test Case 3 : if the input is `MCMXCIV` then the output would be `1994`



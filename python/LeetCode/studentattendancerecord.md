# Leet Code Student Attendance Record Problem 

---

## Problem

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

- 'A': Absent.
- 'L': Late.
- 'P': Present.
  
The student is eligible for an attendance award if they meet both of the following criteria:
- The student was absent ('A') for strictly fewer than 2 days total.
- The student was never late ('L') for 3 or more consecutive days.
- Return true if the student is eligible for an attendance award, or false otherwise.

--- 

## Progress Method 

- first we must create 2 variables to check the student's late and absent counts which both starts from 0. 
- next we need to loop through the string (s) to check the late and the absents.
- using if function we check each string if there are absents or late in the attendance record.
  - if there's "A" then we add 1 to the absent count and if the absent is more than 2 we return False.
  - if there's "L" then we add 1 to the late count and if the late count is 3 then we also return False.
  - else, then we reset the late count to 0.
- Lastly, we return True if the absent is less than 2 and late less than 3

--- 

## Code 
>
    def checkRecord(self, s: str) -> bool:
        late = 0 
        absent = 0 

        for i in range(len(s)):
            char = s[i]
            if char == "A":
                absent += 1 
                if absent >= 2: 
                    return False
            if char == "L":
                late += 1 
                if late == 3:
                    return False
            else:
                late = 0 
        return absent < 2 and late < 3

## Result 
if the input is  `"PPALLP"` then the output would be `true`. 
Meanwhile if the input is `"PPALLL"` then the output would be `false`. 


    


# Baseball Game Coding Test Problem [260219]

---

## Problem 
Write a game that matches computer-generated three-digit numbers. 

Game Rules : 
- The computer generates a non-overlapping three-digit number(100-999)
- User enters 3-digit numbers
- 1 Strike if both the numbers and the positions are correct
- 1 Ball if the number is correct, but if the position is different
- If 3 Strike comes out, then the game is over

Validation of input : 
1. When entering non-numerical characters -> wrong input
2. If you enter a mistake -> wrong input
3. Under 100 or above 999 -> wrong input
4. When entering duplicate digits -> wrong input

Termination Condition : 
- Exit immediately when 0 is entered during the game

---

##   Progress Method 

- the helping function for getting the random number is already available.
- first we define a function called is_digit
  - inside we first try to change the user input into an integer
  - if there's an error in the try then the conversion has failed 
- then we define the second function which is called is_between_100_and_999
  - this function is used to check for the input number to make sure that the input number is between 100 and 999
  - inside this function we return the user input as an integer if the number is between 100 and 999
- for the third function which is called is_duplicated_number
  - we want to compare each number to make sure there's no duplicated number in each digits
  - therefore we compare the first digit with the second one, the first digit and the third one and the second digit with the third one.
- for the fourth function which is called is_validated_number
  - we want to check if the numbers are valid which means the user input has to be a valid integer, in between 100 and 999 and also not a duplicated number.
  - therefore, we just use all 3 of the functions that we have defined previously
- for the next function which is called get_not_duplicated_three_digit_number
  - first we want to start a loop
  - next we want to get 3 random numbers using the helping function (get_random_number)
- next we create another function called get_strikes_or_balls
  - here we want to compare each digits from the user input and the random number to get the amount of strikes and ball
  - first we create 2 variables which are strike and ball. these variables are used as counters and therefore they both starts at 0
  - next we start a loop over the first, second and third digit positions
  - if the user input number and the random number is the same then add 1 to strike
  - else if the user input is in the random number then add 1 to ball
  - next we return the number of strike and ball
- the next function is is_yes for one more input
  -  first we return the input in lower case and also check if the input is against the allowed values
- next function is is_no for one more input
  - first we return the input in lower case and also check if the input is against the allowed values
- the last function is the main function which is used to run this whole game
  - first we print "Game Start" at the start of the game
  - next we want to get and print the random number using the get_not_duplicated_three_digit_number function
  - then we are going to start a loop to add the user input number with a few conditions towards the user input number :
    - if the user inputs 0 then we're going to print "Game Over"
    - and if the user input is not a validated number then we're going to print "Wrong Input"
  - next  we want to calculate the amount of strikes and balls by using the get_strikes_or_balls function
  - the game has a condition that if the strike reaches 3 then we print "Game Over"
  - next we want to add the restart game option
    - using the is_yes and is_no function we check the user input and if the input is other than that then we print "Wrong Input"
    - lastly we want to print the result for the strike and the ball counter. 

---

## Code 

>
    def get_random_number():
      return random.randint(100, 999)

    def is_digit(user_input_str):     
      try:
        int(user_input_str)
        return True
      except:
        return False
        
    def is_between_100_and_999(user_input_str):
      return 100 <= int(user_input_str) < 1000

    def is_duplicated_number(three_digit_str):
      return (
        three_digit_str[0] == three_digit_str[1]
        or three_digit_str[0] == three_digit_str[2]
        or three_digit_str[1] == three_digit_str[2]
      )
    
    def is_validated_number(user_input_str):
      return (
        is_digit(user_input_str) and is_between_100_and_999(user_input_str)
        and not is_duplicated_number(user_input_str)
      )
    
    def get_not_duplicated_three_digit_number():
      while True:
        number = get_random_number()
        if len(set(str(number))) == 3: 
            return number
            
    def get_strikes_or_balls(user_input, random_number):
      strike = 0 
      ball = 0 

      for i in range(3):
        if user_input[i] == random_number[i]:
            strike += 1 
        elif user_input[i] in random_number:
            ball += 1
    
      return [strike, ball]

    def is_yes(one_more_input):
      return one_more_input.lower() in ("y", "yes")

    def is_no(one_more_input):
      return one_more_input.lower() in ("n", "no")

    def main():       
      print ("Game Start!")
      random_num = str(get_not_duplicated_three_digit_number())
      print(f"{random_num}")

      while True: 
        user_input = input("Input Number:").strip()

        if user_input == "0":
            print ("Game Over")
            return

        if not is_validated_number(user_input):
            print ("Wrong Input")
            continue

        strike, ball = get_strikes_or_balls(user_input, random_num)

        if strike == 3: 
            print (" 3 Strike ! ")

            while True: 
                again = input("play again? (y/n):").strip()
                if is_yes(again):
                    main()
                    return
                if is_no(again):
                    print("Game Over")
                    return 
                else: 
                    print("Wrong Input")
        else:
            print(f"result : {strike} strike, {ball}ball")

--- 

## Result 

For example, the computer generated number is 534 :
- If the user input is `345`, then the result is `0 strike, 3 ball`
- If the user input is `543`, then the result is `1 strike, 2 ball` 

--- 





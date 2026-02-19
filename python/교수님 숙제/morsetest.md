# Morse Coding Test Problem [260219]

--- 

## Problem 

Write a program that translates Morse Code. When the user enters the alphabet, it transforms into a morse code, and when the morse code is entered, it transforms into an alphabet.

Rules : 
1. alphabet - morse code conversion :
   - spacing a space between each character
   - spacing two spaces between words
   - delete punctuation marks
  
2. morse code - alphabet conversion :
   - space one space : character separation
   - space two spaces : word separation
  
3. validation of input :
   - alphabet : error when including numbers or special characters
   - morse code : error when including external characters
  
---

## Progress Method 
- the helping function (get_morse_code_dict) and (get_help_message) is already available
- the first function that we need to define is the is_help_command
  - the user input will be changed into upper case and the space will be removed, and then it will be checked if the user inputs H or HELP
- the second fuction that we need to define is the is_validated_english_sentence function
  - first we make an empty string to later on store the valid characters called clean
  - next we loop through each characters in the user input
  - if the character is a digit then return false
  - if the character is a character or a space, then add it to clean
  - if the character is a punctuation then skip it
  - if the character is anything else then return false
  - lastly we remove the space in "clean"
- the third function that we need to define is the is_validated_morse_code function
  - first we create a set of the allowed characters with the name allow
  - next we want to get the morse dictionary and a set of just the morse dictionary values
  - next we loop through each characters in the user input
    - if the character is not in allow then we return false
  - next we want to clean the user input by removing outer spaces and also split it by spaces
  - we start another loop and then we seperate each letters in the word
    - and then we loop each letter and check if it's not in the dictionary then we return false
- the next function is the get_cleaned_english_sentence
  - first we create an empty string for the result
  - next we loop each character in raw english sentence
    - if the character is letter and space then we add it to res
    - next we return res in an uppercase format and remove the outer spacing there
- the next function is encoding_character function
  - first we need to get the morse dictionary
  - next we convert the character into uppercase and then return the morse code
- the next function is decoding_character function
  - first we need to get the morse dictionary
  - next we loop the dictionary
    - if the value is the same as the morse character then we return the english letter
- the next function is encoding_sentence function
  - first we use the get_cleaned_english_sentence to get the clean input
  - next we want to split it into words
  - next we create an empty list to store the result
  - after that we want to loop through each word
    - then make an empty list called encoded_letter to store the encoded letters
    - then we also need to loop through each characters
      - we want to encode each characters and then combine them with spaces
 - the next function is the decoding_sentence
   - first we want to remove the spaces and also split it
   - next we create an empty list to store the decoded words
   - after that we loop through the words
     - then we split the words into letters
     - we also need to create another empty list to store the decoded letters
     - next we loop through each letter
       - then we want to decode each letter and combine them into the decoded words
- the last function is the main function
  - first we start a loop using the while function
    - next we want to get the user input
    - if the user input 0 then we stop the loop
    - if the user input is the help command then we print the get help message function
    - if the user input is a validated english sentence then we print the encoding sentence for the user input
    - if the user input is a validated morse code then we print the decoding sentence for the user input
    - otherwise we print out "Wrong Input"

---

## Code 

>
    def get_morse_code_dict():
      morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--.."
      }
      return morse_code

    def get_help_message():
      message = "===== 모스 부호 표 =====\n"
      morse_code = get_morse_code_dict()
      counter = 0
      for key, value in sorted(morse_code.items()):
        message += f"{key}: {value:<5} "
        counter += 1
        if counter % 5 == 0:
            message += "\n"
      return message

    def is_help_command(user_input):
      return user_input.strip().upper() in ("H", "HELP")


    def is_validated_english_sentence(user_input):
      clean = ""
    
      for c in user_input:
        if c.isdigit():
            return False 
        if c.isalpha() or c == " ":
            clean += c
        elif c in ".,!?":
            continue
        else:
            return False
    return clean.strip() != ""

    def is_validated_morse_code(user_input):
      allow = {"-", ".", " "}
      morse_dict = get_morse_code_dict()
      valid = set(morse_dict.values())

      for c in user_input:
        if c not in allow:
            return False
        
       w = user_input.strip().split(" ")
      for word in w : 
        letters = word.split()
        for letter in letters :
            if letter not in valid:
                return False
    return True

    def get_cleaned_english_sentence(raw_english_sentence):
      res = ""
      for c in raw_english_sentence:
        if c.isalpha() or c == " ":
            res += c
    return res.strip().upper()

    def encoding_character(english_character):
      morse_dict = get_morse_code_dict()
      return morse_dict[english_character.upper()]
    
    def decoding_character(morse_character):
      morse_dict = get_morse_code_dict()
      for key, value in morse_dict.items():
        if value == morse_character:
            return key
    
    def encoding_sentence(english_sentence):
      clean = get_cleaned_english_sentence(english_sentence)
      w = clean.split()

      encoded = []
      for word in w:
        encoded_letter = []
        for c in word:
            encoded_letter.append(encoding_character(c))
        encoded.append(" ".join(encoded_letter))

      return " ".join(encoded)

    def decoding_sentence(morse_sentence):
      w = morse_sentence.strip().split(" ")

      decoded_word = []
      for word in w:
        letters = word.split()
        decoded_letter = []
        for letter in letters : 
            decoded_letter.append(decoding_character(letter))
        decoded_word.append("".join(decoded_letter))
    
      return " ".join(decoded_word)
    
    def main():
      while True: 
        user_input = input("Input Message (H = Help, 0 = Exit)")

        if user_input == "0":
            break

        if is_help_command(user_input):
            print(get_help_message())
            return
        
        if is_validated_english_sentence(user_input): 
            print(encoding_sentence(user_input))

        if is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        
      else:
            print("Wrong Input")

---

## Result 

- If the user input is `test` then the result would be `- . ... -`
- If the user input is `- . ... -` then the result would be `T E S T` 

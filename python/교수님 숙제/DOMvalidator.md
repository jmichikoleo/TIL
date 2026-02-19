# DOM Validator Test [260219]

--- 

## Problem 

Write a program to verify that the DOM structure of a simple HTML / XML like document given as a string is correct  

DOM Rules:
- tag is in <tag> or </tag> format
- tag names consist of only uppercase letters (e.g. A, DIV, SPAN)
- all start tags </tag> require a corresponding end tag </tag>
- tags must overlap correctly
- blank and plain text do not affect validation

---

## Progress Method 
- the first function that we need to define is the tokenize function
  - inside we create an empty list called token which is going to store the tokens
  - next we create an index variable and set it to 0
  - also we create another variable which stores the length of the string
  - next we create a loop that runs for as long as i is within the string
    - then we want to check if the current character is "<"
    - after that we find the ">" from the position i until it is found and we return the index of it if its found
      - if it's not found then return -1 
      - if the close_idx is -1 then we exit the function
    - next we want to extract the tag name inside the <>
    - also we need to check if it's a close tag (</>) so if the tag_content starts with "/"
      - then we add an END token and removes the "/"
      - otherwise we add START token with the tag name
      - next we move the index past the >
    - else we create start which marks the start of the text
      - then we create a loop which continues until the end of string or the start of a tag
      - we want it to move one character at a time
      - next we need to extract the text from the tags
        - if the text is not empty then we add the text token
  - next we just return all of the tokens
- the second function is the is_valid_tag_name function
  - in order to check on whether or not the tag name is valid or not, we return the tag_name as a bool and check it using the isalpha() and isupper() function
- the third function is the validate_dom function
  - if the dom string is empty then return false
  - next we want to use the tokenize function for the input
    - after that we check if there's an error or not at the parsing, if yes then return false
  - next we create an empty list called stack
  - after that we loop through each token
    - if the token type is start then
      - check if the value is not a valid tag name, then return false because of invalid name
      - next we add the value to stack
    - if the token type is end then
      - we check if the value is not a valid tag name, then return false because of invalid name
      - if no opening tag is available, then return false because unopened
      - if the opening tag and the closing tag does not match, then return false because of wrong nesting
    - after processing all of the above, we check again if there are unclosed tags, if yes then return false because of unclosed
- the next function is the get_error_message function
  - first we create a dictionary for the error message called messages
  - then we return the error message based on the error type
- the next function is the is_yes function
  - we return the input in lower case, remove the spaces and check the allowed yes values
- the next function is the is_no function
  - we return the input in lower case, remove the spaces and check the allowed no values
- the last function is the main function
  - first we start a loop
    - next we check the user input and validate the DOM string
    - if it's valid then print "Result: Valid DOM structure"
    - if error because of empty input then print "Wrong Input"
    - otherwise print invalid DOM structure with the error message
  - next we add the restart function
  - if the user wants to continue (is_yes) then continue
  - if the user doesn't want to continue (is_no) then print "Program Closing"
  - Otherwise print "Wrong Input" 

---

## Code

>
      def tokenize(dom_string):
        tokens = []
        i = 0
        n = len(dom_string)

        while i < n:
          if dom_string[i] == "<":
            close_idx = dom_string.find(">", i)
            if close_idx == -1:
                return None

            tag_content = dom_string[i + 1:close_idx]

            if tag_content.startswith("/"):
                tokens.append(("END", tag_content[1:]))
            else:
                tokens.append(("START", tag_content))

            i = close_idx + 1
        else:
            start = i
            while i < n and dom_string[i] != "<":
                i += 1
            text = dom_string[start:i]
            if text:
                 tokens.append(("TEXT", text))
      return tokens
    
    def is_valid_tag_name(tag_name):
      return bool(tag_name) and tag_name.isalpha() and tag_name.isupper()
   
    def validate_dom(dom_string):
      if dom_string == "" :
        return False, "EMPTY"

    tokens = tokenize(dom_string)
    if tokens is None:
        return False, "PARSE"

    stack = []

    for token_type, value in tokens:
        if token_type == "START":
            if not is_valid_tag_name(value):
                 return False, "INVALID_NAME"
            stack.append(value)

        elif token_type =="END":
            if not is_valid_tag_name(value):
                return False, "INVALID_NAME"
            if not stack:
                return False, "UNOPENED"
            if stack.pop() != value:
                return False, "NESTING"

      if stack:
        return False, "UNCLOSED"

      return True, ""

    def get_error_message(error_type):
      messages = {
        "EMPTY" : "empty input string",
        "PARSE" : "parse error",
        "INVALID_NAME" : "invalid tag name",
        "UNOPENED" : "no opening tag",
        "UNCLOSED" : "tag unclosed",
        "NESTING" : "wrong nesting tag"
    }

      return messages.get(error_type,"unknown error")
   
    def is_yes(user_input):
      return user_input.strip().lower() in ("y", "yes")

    def is_no(user_input):
      return user_input.strip().lower() in ("n", "no")

    def main(): 
      while True:
        dom_string = input("\nInput DOM string: ")
        is_valid, error = validate_dom(dom_string)

        if is_valid:
            print("Result: Valid DOM structure")
        else:
            if error =="EMPTY":
                print("Wrong Input")
            else:
                 print(f"Result: Invalid DOM structure - {get_error_message(error)} ")

        answer = input("\nValidate again ? (Y/N)")

        if is_yes(answer):
            continue
        elif is_no(answer):
            print("Program closing")
            break
        else:
            print("Wrong Input")

---

## Result

- If the input is `<A>test</A>` then the output would be `Result: Valid DOM structure`
- If the input is `<A><B>text</B></A>` then the output would be `Result: Valid DOM structure`
- If the input is `<A>text</A><B>more</B>` then the output would be `Result: Valid DOM structure`
- If the input is `<DIV><SPAN>hello</SPAN></DIV>` then the output would be `Result: Valid DOM structure`
- If the input is `<A><B></A></B>` then the output would be `Invalid DOM structure - wrong nesting tag`
- If the input is `<A>text` then the output would be `Invalid DOM structure - tag unclosed`
- If the input is `</A>` then the output would be `Invalid DOM structure - no opening tag`
- If the input is `<A><B>text</A></B>` then the output would be `Invalid DOM structure - wrong nesting tag`
- If the input is `<123>text</123>` then the output would be `Invalid DOM structure - invalid tag name` 

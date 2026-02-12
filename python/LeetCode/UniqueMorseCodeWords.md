# Leet Code Unique Morse Code Words Problem [260212]

--- 

## Problem 

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: 

- 'a' maps to ".-",
- 'b' maps to "-...",
- 'c' maps to "-.-.", and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below : 
`[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]`

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter. 

- For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the transformation of a word.

- Return the number of different transformations among all words we have.

---

## Progress Method 

- first we create a dictionary for the morse code and each of the alphabet.
- next, we need to create an empty list (wording). 
- next, we want to loop each word in the input list of words and put it inside of the variable(w).
- after that we loop through each character in the word, check the translation in the dictionary.
- then we add each character until all the characters are translated.
- lastly, we convert the list into a set and counts how many unique items inside. 

---

## Code
>
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

         morse_dict = { 
            "a" : ".-",
            "b" : "-...",
            "c" : "-.-.",
            "d" : "-..",
            "e" : ".",
            "f" : "..-.",
            "g" : "--.",
            "h" : "....",
            "i" : "..",
            "j" : ".---",
            "k" : "-.-",
            "l" : ".-..",
            "m" : "--",
            "n" : "-.",
            "o" : "---",
            "p" : ".--.",
            "q" : "--.-",
            "r" : ".-.",
            "s" : "...",
            "t" : "-",
            "u" : "..-",
            "v" : "...-",
            "w" : ".--",
            "x" : "-..-",
            "y" : "-.--",
            "z" : "--.."
        }

        wording = []
        
        for word in words: 
            w = ""

            for i in word: 
                w+= morse_dict[i]

            wording.append(w)

        return len(set(wording))

  ---

  ## Result 

  - Test Case 1 : if the input is `["gin","zen","gig","msg"]` then the output is `2`.
  - Test Case 2 : if the input is `["a"]` then the output is `1`.

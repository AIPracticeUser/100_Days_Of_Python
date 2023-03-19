# Caesar Cipher
AIM: Build a Caesar Cipher and learn about functions

## Positional Arguments
![image](https://user-images.githubusercontent.com/100339175/226138663-64a2fd5e-74d6-4d09-9e03-a2cabd94cd0d.png)

## Keyword Arguments
![image](https://user-images.githubusercontent.com/100339175/226138685-112c4ea1-3783-42e0-890f-c6672fd68727.png)

##Exercise 1: Prime Number Checker
### Instructions

LINK :  https://replit.com/@LightGamer1/Day8Prime-Number-Check?v=1

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.



### Caesar Cipher Part 1
Working Program: 

https://replit.com/@LightGamer1/caesar-cipher-1-start?v=1

CODE: 
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  new_string = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    new_position = position + shift_amount
    if new_position >= 26:
      new_position -= 26
    new_string += alphabet[new_position]
  print(f"The encrypted string is {new_string}")
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)
```

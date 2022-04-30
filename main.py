alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    # Replicate the initial list of 'a' to 'z' twice ----> so that won't out of range e.g: shift letter 'w' by 5 spaces will still be 'b' 

def caesar(start_text, shift_amount, cipher_direction):               # Create function with input parameters 
  
  end_text = ""                                   # Create empty string so that i can append to it afterwards 
  if cipher_direction == "decode":
    shift_amount *= -1                         # because decode means shift backwards ---> 5 will become -5, otherwise shift_amount will remain at 5 for encode
  for char in start_text:              # For letter in message 
    if char in alphabet:               #if letter in message belongs to an element in the list alphabet:
      position = alphabet.index(char)           # find the index of that letter in the list 
      new_position = position + shift_amount        # new index 
      end_text += alphabet[new_position]        # encoded/decoded text 
    else:                              #if letter in message dont belong in the list alphabet: e.g: number/space/symbol  -------> will remain in end_text
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")           # Using f-string to insert the final encoded/decoded text
  

from art import logo                     # Import and print the logo from art.py when the program starts.
print(logo)                             
                                                          #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
                                                          #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
                                                          #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
                                                          #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 


loop_again = True         # create FLAG VARIABLE, assign it True
while loop_again:         #While True, following will be executed
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")                        # INPUT FOR PARAMETERS 
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

                                                          #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
                                                          #Try running the program and entering a shift number of 45.
                                                          #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
                                                          #Hint: Think about how you can use the modulus (%).
  
  
  shift = shift % 26        # Remainder is the value of shift -----> multiple of 26 (total lenght of alphabet
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)                        # CALLING THE FUNCTION
  
  
  
  try_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()            # FOR TODO-4 
  if try_again == 'no':
    loop_again = False      # FLAG VARIABLE: Will not run the while loop
    print("Goodbye.")
  elif try_again == 'yes':
    loop_again = True 
  else:
    loop_again = False 
    print("You have typed an invalid message. Try again.")
     
    

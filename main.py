import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: [DONE] Import and print the logo from art.py when the program starts. [DONE]
#TODO-2: [DONE] What if the user enters a shift that is greater than the number of letters in the alphabet? [Done during part 2]
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

        #TODO-3:[DONE] What happens if the user enters a number/symbol/space?
            #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            #e.g. start_text = "meet me at 3"
            #end_text = "•••• •• •• 3"
#TODO-4: [DONE] Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'. 
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. [DONE]


def ceasar(plain_text, shift, direction):
    cypher_text = ""
    remainder_is_larger = False
    list_length = len(alphabet)
    encode = decode = False

    if direction == "encode":
        encode = True
    elif direction == "decode" :
        decode = True
    
    for letter in plain_text:
        if letter not in alphabet:
            cypher_text += letter
        else:
        
        # check if is a number/space/symbol
            #if yes, insert the given character into cypher_text
            # if not, index = alphabet.index(letter)
            # indent all code below in this elif
        
            index = alphabet.index(letter)
            sum_shift_index = index + shift
            remainder_shift = shift
            print(f"\n ERROR letter: {alphabet[index]}")
    
            if sum_shift_index > list_length-1:
                remainder_is_larger = True
    
                while remainder_is_larger:
                    if index == 0:
                        while remainder_is_larger:
                            if remainder_shift < list_length:
                               remainder_is_larger = False
                            else:
                                print(f"\n WHILE REM IS LARGER: remainder shifts before: {remainder_shift}")
                                remainder_shift -= list_length
                                print(f" WHILE REM IS LARGER: remainder shifts after: {remainder_shift}")
    
                    else:
                        if encode:
                            remainder_shift = shift - (list_length - index)
                        elif decode:
                            print(f"\nremainder shifts: {remainder_shift}")
                            print(f"original shift: {shift}")
                            print(f"index: {index}")
                            remainder_shift = shift - index
                            print(f"remainder shifts after sub: {remainder_shift}")
                        else:
                            print("Direction is not valid")
                        index = 0
            
            if encode:
                index += remainder_shift
            if decode:
                print(f"\nremainder shifts: {remainder_shift}")
                print(f"\nindex before subtraction with remainder: {index}")
                index -= remainder_shift
            print(f"\nletter insertion index after subtr: {index}")
            cypher_text += alphabet[index]
            
        print(f"\nResult: {cypher_text}")

# END ceasar(plain_text, shift, direction)

restart = True
print(art.logo)
while restart:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceasar(text, shift, direction)

    choice = input("\n Would you like to go again? ").lower()
    if (choice == "no") or (choice == "n"):
        restart = False
        print("\nGoodbye")
        
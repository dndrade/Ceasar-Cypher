import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
            index = alphabet.index(letter)
            sum_shift_index = index + shift
            remainder_shift = shift
    
            if sum_shift_index > list_length-1:
                remainder_is_larger = True
    
                while remainder_is_larger:
                    if index == 0:
                        while remainder_is_larger:
                            if remainder_shift < list_length:
                               remainder_is_larger = False
                            else:
                                remainder_shift -= list_length
                    else:
                        if encode:
                            remainder_shift = shift - (list_length - index)
                        elif decode:
                            remainder_shift = shift - index
                        else:
                            print("Direction is not valid")
                        index = 0       
            if encode:
                index += remainder_shift
            if decode:
                index -= remainder_shift
            cypher_text += alphabet[index]
            
        print(f"\nResult: {cypher_text}")

# END ceasar(plain_text, shift, direction)

restart = True
print(art.logo)
while restart:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= len(alphabet)
    
    ceasar(text, shift, direction)

    choice = input("\n Would you like to go again? ").lower()
    if (choice == "no") or (choice == "n"):
        restart = False
        print("\nGoodbye")  

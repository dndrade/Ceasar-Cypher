alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). [DONE]
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values. [DONE]


def ceasar(plain_text, shift, direction):
    cypher_text = ""
    remainder_is_larger = False
    list_length = len(alphabet)
    encode = False
    decode = False

    if direction == "encode":
        encode = True
    elif direction == "decode" :
        decode = True
    
    for letter in plain_text:
        index = alphabet.index(letter)
        sum_shift_index = index + shift
        remainder_shift = shift

        if sum_shift_index > list_length:
            remainder_is_larger = True

            while remainder_is_larger:
                if index == 0:
                   while remainder_is_larger:
                       remainder_shift -= list_length

                       if remainder_shift < list_length:
                           remainder_is_larger = False

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


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

ceasar(text, shift, direction)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt (plain_text, shift):
    cypher_text = ""
    remainder_is_larger = False
    
    for letter in plain_text:
        #print(f"current letter: {letter}")
        index = alphabet.index(letter)
        # for each letter, check if the shift will be out of range
        # by adding its index alphabet and shift
        pre_sum_of_index_shift = index + shift 

        #subtract 1 when comparing len() with list index value
        if pre_sum_of_index_shift > (len(alphabet)-1): 
            remainder_shift = shift
            remainder_is_larger = True

            while remainder_is_larger != False:
                if index == 0:
                    while remainder_is_larger:
                        remainder_shift -= len(alphabet)
                        if remainder_shift < len(alphabet):
                            remainder_is_larger = False
                            index += remainder_shift
                            cypher_text += alphabet[index]
                else:
                    for iteration in range(index, (len(alphabet)-1)):
                        remainder_shift -= 1
                    
                    index = 0
                    remainder_shift -= 1
        else:
            index += shift
            cypher_text += alphabet[index]
    print(cypher_text)

def decrypt (plain_text, shift):
    cypher_text = ""
    # remainder_shift = shift
    remainder_is_larger = False
    #zero_index = False
    for letter in plain_text:
        #print(f"current letter: {letter}")
        print("\n\n [LINE 42] FOR LOOP") #debug
        index = alphabet.index(letter)
        print(f"\nCurrent text letter {letter}") #debug
        print(f"\nCurrent index in aphabet {index}") #debug
        # negative numbers have the end of list as starting point
        # if shift is larger than list size, 
        # it will be out of range just like positives
        # to perform an interation when shift > list size,
        # perform 1st shift by making index = 0, subtract shift - index
        # if still shift > l size, keep subtracting by
        # remaining_shift by l size until remaining_shift is smaller than l size
        # this way, shifting will only be ever performed twice
        if shift > len(alphabet):
            remainder_shift = shift
            remainder_is_larger = True
            print("\nshift > len(alphabet)") #debug

            # while remaining_is_larger != False
            while remainder_is_larger != False: 
                print("\n [LINE 60] WHILE remainder_is_larger = True") #debug
                # if index is at the correct place (0), do the operation
                if index == 0:
                    #zero_index = True
                    print("\n if index == 0") #debug
                    print(f"remainder_shift before sub: {remainder_shift}") #debug
                    while remainder_is_larger:
                        print("\n [LINE 67] WHILE remainder_is_larger = True") #debug
                        remainder_shift -= (len(alphabet))
                        print(f"remainder_shift after sub: {remainder_shift}") #debug
                        if remainder_shift < (len(alphabet)):
                            remainder_is_larger = False
                            print("\nremainder_shift < (len(alphabet)")    #debug
                            print("remainder_is_larger = False")    #debug
                            index -= remainder_shift
                            print(f"index: {index}")           #debug
                            cypher_text += alphabet[index]
                            print(f"cypher char to be inserted: {alphabet[index]}") #debug
    
                # if index isn't at the correct place (0), move it to 0
                else:
                    print("\n else index is not 0, make it 0") 
                    print(f"remainder_shift before update: {remainder_shift}") 
                    # subtract index number by remainder_shifts
                    remainder_shift -= index
                    print(f"remainder_shift after update: {remainder_shift}")
                    print(f"\n index before update: {index}") 
                    # update index value to 0
                    index -= index
                    print(f"\n index is updated (should be 0): {index}") 

        # if shift is within list size range
        else:
            print(f"\n index ({index}) is within list size range") 
            # iterate from right through left 
            # by subtracting current index and shift number
            index -= shift
            print(f"\n updated index ({index}) is within list size range") 
            # insert the character into cypher
            cypher_text += alphabet[index]
            print(f"cypher char to be inserted: {alphabet[index]}") #debug

    print(f"Final cypher: {cypher_text}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    decrypt(text, shift)
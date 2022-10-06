import random
def password():
    password = ''
    length = 0
    
    characters = (
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
                    '!', '@', '#', '$', '%', '^', '&', '*', '(' ,')' ,'{' ,'}' ,'[' ,']' , '<', '>', '?',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 
                  )
    
    while length < 8 or length > 1000:
        try:
            length = int(input('How many characters would you like?'))
            break
        except ValueError:
            print ('Please choose an integer')
        if length < 8:
            print('Please pick a number larger than 7')
        elif length > 1000:
            print("please pick a smaller number")
     
    
    
    for z in range(length):
        password += random.choice(characters)
    print(password)


def main():
    password()


main()
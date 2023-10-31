#Abdullah Islam

def encode(password):
    num = ''
    for i in range(8):

        if str(int(password[i])) == '7':
            num += '0'
        elif str(int(password[i])) == '8':
            num += '1'
        elif str(int(password[i])) == '9':

            num += '2'
        else:
            num += str(int(password[i]) + 3)

    return num


# James Chau
def decode(num):
    for i in num:
        result = ''
        for i in num:
            if i == '2':
                result += '9'
            elif i == '1':
                result += '8'
            elif i == '0':
                result += '7'
            else:
                result += str(int(i) - 3)
        return result


print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
user_input = input("Please enter an option: ")

while user_input != '3':

    if user_input == '1':
        num_to_encode = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n")

    elif user_input == '2':
        print(f"The encoded password is {encode(num_to_encode)}, and the original password is {decode(encode(num_to_encode))}.\n")

    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
    user_input = input("Please enter an option: ")
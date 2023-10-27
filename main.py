#Abdullah Islam

def encode(password):
    encoded_num = ''
    for i in range(8):

        if str(int(password[i])) == '7':
            encoded_num += '0'
        elif str(int(password[i])) == '8':
            encoded_num += '1'
        elif str(int(password[i])) == '9':

            encoded_num += '2'
        else:
            encoded_num += str(int(password[i]) + 3)

    return encoded_num

# James Chau
def decode_rle(rle_data):
    decode = []
    for i in range(0, len(rle_data), 2):
        value = rle_data[i]
    for t in range(0, value):
        decode.append(rle_data[i+1])
    return decode


user_input = input('''Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: ''')


while user_input != '3':
    if user_input == '1':
        num_to_encode = input('Please enter your password to encode: ')
        print('Your password has been encoded and stored!')
    elif user_input == '2':
        print(f'The encoded password is {encode(num_to_encode)}, and the original password is {num_to_encode}.')

    user_input = input('''\nMenu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: ''')
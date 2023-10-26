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




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

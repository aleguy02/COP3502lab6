# Alejandro Villate

def encode(data: str):
    encoded_data = ''
    for digit in data:
        digit = int(digit) + 3
        encoded_data += str(digit)
    return encoded_data
def decode(data: str):
    decoded_data = ""
    for digit in data:
        digit = int(digit) - 3
        decoded_data += str(digit)
    return decoded_data
    pass

menu = "Menu\n" \
       "-------------\n" \
       "1. Encode\n" \
       "2. Decode\n" \
       "3. Quit\n"


_input = -1
while _input != 3:
    print(menu)
    _input = int(input('Please enter an option: '))
    if _input == 1:
        password = input('Please enter your password to encode: ')
        password = encode(password)  # encodes password
        print("Your password has been encoded and stored!")
    elif _input == 2:
        print(f'The encoded password is {password} and the original password is {decode(password)}.')
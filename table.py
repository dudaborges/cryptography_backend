table = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '.': 27, ',': 28, '!': 29, '?': 30, ' ': 31, 'Ç': 32, 'Á': 33, 'É': 34, 'Í': 35, 'Ó': 36, 'Ú': 37, 'Â': 38, 'Ê': 39, 'Ô': 40}

coding_matrix = [[4, 1], 
                [3, 1]]

decoder_matrix = [[1, -1], 
                  [-3, 4]]

print('=-' * 40)
message = input('\033[1;32;40mEnter the message to be encrypted:\33[m \n').upper()

while len(message) < 4:
    message = input('[ERROR] Enter more than 4 characters: ').upper()

def original_message():
    message_matrix = []
    letters = list(message)
    for letter in letters:
        if letter in table:
            message_matrix.append(table[letter])

        else: 
            message_matrix.append(0)

    if len(message) % 2 != 0:
        message_matrix.append(table[' '])
    
    return message_matrix

def message_encoding():
    message_matrix = original_message()
    half_list = len(message_matrix) // 2
    first_line = message_matrix[:half_list]
    second_line = message_matrix[half_list:]
    encoded_first_line = []
    encoded_second_line = []

    for i, num in enumerate(first_line):
        encoded_num_ft = coding_matrix[0][0] * first_line[i] + coding_matrix[0][1] * second_line[i]
        encoded_first_line.append(encoded_num_ft)

    for i, num in enumerate(second_line):
        encoded_num_sd = coding_matrix[1][0] * first_line[i] + coding_matrix[1][1] * second_line[i]
        encoded_second_line.append(encoded_num_sd)


    return encoded_first_line, encoded_second_line


def message_decoding():
    encoded_first_line, encoded_second_line = message_encoding()
    joint = []
    decoded_message = []
    
    for i, num in enumerate(encoded_first_line):
        decoded_num_ft = decoder_matrix[0][0] * encoded_first_line[i] + decoder_matrix[0][1] * encoded_second_line[i]
        joint.append(decoded_num_ft)

    for i, num in enumerate(encoded_second_line):
        decoded_num_sd = decoder_matrix[1][0] * encoded_first_line[i] + decoder_matrix[1][1] * encoded_second_line[i]
        joint.append(decoded_num_sd)

    for num in joint:
        for key, value in table.items():
            if value == num:
                decoded_message.append(key)
    
    return decoded_message


option = 0
def options(option):

    if option == 1:
        print('\n\033[1;30;46mMensagem Original:\33[m\n')
        print(original_message())

    elif option == 2:
        print('\n\033[1;30;41mMensagem Codificada:\33[m\n')
        print(message_encoding())
    elif option == 3:
        print('\n\033[1;30;42mMensagem Decodificada:\33[m\n')
        print(message_decoding())
    elif option == 4:
        print('leaving the program...')
    else:
        print('\033[1;31;40m[ERROR] Option not found.\33[m')


while option != 4:

    print('''
    [1] See original message
    [2] Encode message
    [3] Decode message
    [4] Exit
    ''')

    try:
        option = int(input('Enter your option: '))
        options(option)
    except:
        print('\033[1;31;40m[ERROR] Enter the numeric value.\33[m')
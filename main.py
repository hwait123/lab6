# Hannah Wait
# encode the password
def encoder(password):
    # convert password to str
    password = str(password)

    # initialize new password string
    new_password = ''

    # iterate through old password
    for num in password:
        # add 3 to each number and append to new password
        num = int(num) + 3
        new_password += str(num)

    return new_password


def decoder(password):
    password = str(password) #Katherine: converting again to a string
    decode_password = ''
    for i in password: #reverse of the encoder function
	decode_password += int(i)-3
    return decode_password


# print menu
def print_menu():
    print()
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


if __name__ == '__main__':

    # initialize user_password
    user_password = ''

    while True:

        # display menu
        print_menu()

        # accept user input
        user_selection = int(input('Please enter an option: '))

        # encode password
        if user_selection == 1:

            # prompt user for password
            user_password = input('Please enter your password to encode: ')

            # transform and store password
            user_password = encoder(user_password)

            # print acceptance message
            print('Your password has been encoded and stored!')

        # decode password
        elif user_selection == 2:
	    
            # print old and new password
            print(f'The encoded password is {user_password} and the original password is {decoder(user_password)}.')

        # exit
        elif user_selection == 3:
            exit()

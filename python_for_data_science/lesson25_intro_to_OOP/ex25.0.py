

user_name = input("Enter your name: ")
while True:
    response = input('Enter 1 or 2. If you want to look messages - 1, if you want to write - 2')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('File doesn`t exist.')
    elif response == '2':
        new_message = input('Enter your message: ')
        with open('chat.txt', 'a') as file:
            file.write(f'{user_name}: {new_message}\n')
    else:
        print('Unknown command.')



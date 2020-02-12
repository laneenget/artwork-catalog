

def get_choice():
    display_menu()
    while True:
        command = input('Enter a key: ').upper()
        if is_valid(command):
            return command
        else:
            print('Not a valid choice, try again.')

def display_menu():
    print('')
    print('Welcome to the Artwork Catalog!')
    print('Enter a key from the menu to get started.')
    print('1: Add a new artist')
    print('2: Search for artwork by artist')
    print('3: Search for available artwork by artist')
    print('4: Add new artwork')
    print('5: Delete artwork')
    print('6: Change artwork availability')
    print('Q: Quit')

def is_valid():

def show_artwork():

def get_artwork_id():

def get_sale_info():
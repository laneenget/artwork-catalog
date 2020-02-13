from artstore import Artist, Artwork

def get_choice(menu):
    print(menu)
    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command):
            return command
        else:
            print('Not a valid choice, try again.')

def get_artist_info():
    firstname, lastname = input('Enter artist full name: ').split()
    email = input('Enter artist email: ')
    return Artist(firstname, lastname, email)

def get_artwork_info():
    

#def show_artwork():

#def get_sale_info():
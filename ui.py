from artstore import Artist, Artwork, ArtistDB, ArtworkDB

def get_choice(menu):

    print(menu)

    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command):
            return command
        else:
            print('Not a valid choice, try again.')

def get_artist_name():

    first_name, last_name = input('Enter artist full name: ').split()
    return first_name, last_name

def get_artist_info(first_name, last_name):

    email = input('Enter artist email: ')
    return Artist(first_name, last_name, email)

def get_artwork_info(artist_id, title):

    price = float(input('Enter artwork price: '))
    available = input('Enter \'for sale\' or \'sold\': ')

    return Artwork(title, price, available, artist_id)

def get_sale_info():

    while True:
        sale_info = input('Enter \'sold\' or \'available\': ')
        if sale_info.lower() == 'sold':
            return 'sold'
        elif sale_info.lower() == 'available':
            return 'available'
        else:
            print('Type \'sold\' or \'available\'')

def get_artwork_title():
    
    title = input('Enter artwork title: ')
    return title

def show_artwork(artworks):

    if artworks:
        print('')
        for artwork in artworks:
            print(artwork)
        print('')
    else:
        print('No artwork to display.')
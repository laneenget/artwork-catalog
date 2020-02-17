from artstore import Artist, Artwork, ArtistDB, ArtworkDB

def get_choice(menu):

    print(menu)

    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command):
            return command
        else:
            print('Not a valid choice, try again.')

def get_artist_info():

    first_name, last_name = input('Enter artist full name: ').split()
    email = input('Enter artist email: ')
    return Artist(first_name, last_name, email)

def get_artwork_info():

    while True:
        first_name, last_name = input('Enter artist full name: ').split()
        artist_id = ArtistDB().artist_search(first_name, last_name)
    
        if artist_id == -1:
            print('Add the artist to the database first.')
            break

        title = input('Enter artwork title: ')
        price = float(input('Enter artwork price: '))
        available = input('Enter \'for sale\' or \'sold\': ')

        return Artwork(title, price, available, artist_id), first_name, last_name

def get_sale_info():

    while True:
        sale_info = input('Enter \'sold\' or \'available\': ')
        if sale_info.lower() == 'sold':
            return 'sold'
        elif sale_info.lower() == 'available':
            return 'available'
        else:
            print('Type \'sold\' or \'available\'')

def artist_match():

    while True:
        first_name, last_name = input('Enter the artist\'s full name: ').split()

        if ArtistDB().artist_search(first_name, last_name) != "None":
            return first_name, last_name
        else:
            print('That artist is not in the database.')
            break

def artwork_match():

    while True:
        title = input('Enter the artwork title: ')

        if ArtworkDB().artwork_search(title) != "None":
            artwork = ArtworkDB().artwork_search(title)
            return artwork
        else:
            print('That artwork is not in the database.')
            break

def show_artwork(artworks):

    if artworks:
        print('')
        for artwork in artworks:
            print(artwork)
        print('')
    else:
        print('No artwork to display.')
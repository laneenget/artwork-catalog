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

    first_name, last_name = input('Enter artist full name: ').split()
    email = input('Enter artist email: ')
    return Artist(first_name, last_name, email)

def get_artwork_info():

    first_name, last_name = input('Enter artist full name: ').split()

    if Artist.artist_search(first_name, last_name) != "None":
        artist_id = Artist.artist_id
    else:
        print('Add the artist to the database first.')

    title = input('Enter artwork title: ')
    price = float(input('Enter artwork price: '))
    available = input('Enter \'for sale\' or \'sold\': ')

    return Artwork(title, price, available, artist_id)

def get_sale_info():

    while True:
        sale_info = input('Enter \'sold\' or \'available\': ')
        if sale_info.lower() in ['sold', 'available']:
            return sale_info.lower() == 'sold'
        else:
            print('Type \'sold\' or \'available\'')

def artist_match():

    while True:
        first_name, last_name = input('Enter the artist\'s full name: ')

        if Artist.artist_search(first_name, last_name) != "None":
            return first_name, last_name
        else:
            print('That artist is not in the database.')
            break

def artwork_match():

    while True:
        title = input('Enter the artwork title: ')

        if Artwork.artwork_search(title) != "None":
            return title
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
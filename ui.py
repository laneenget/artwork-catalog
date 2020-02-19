from artstore import Artist, Artwork, ArtistDB, ArtworkDB

def get_choice(menu):

    print(menu)

    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command): #Get command
            return command
        else:
            print('Not a valid choice, try again.')

def get_artist_name():

    first_name, last_name = input('Enter artist full name: ').split() #Take artist name input
    return first_name, last_name

def get_artist_info(first_name, last_name):

    email = input('Enter artist email: ') #Take artist email input
    return Artist(first_name, last_name, email) #Create artist object

def get_artwork_info(artist_id, title):

    price = float(input('Enter artwork price: ')) #Take price input
    status = input('Enter \'available\' or \'sold\': ') #Take status input
    if status.lower() == 'available':
        available = 0
    elif status.lower() == 'sold':
        available = 1
    else:
        print('Type \'available\' or \'sold\'.')

    return Artwork(title, price, available, artist_id) #Create object

def get_sale_info():

    while True:
        sale_info = input('Enter \'sold\' or \'available\': ') #Take status input
        if sale_info.lower() == 'sold':
            return 1 
        elif sale_info.lower() == 'available':
            return 0
        else:
            print('Type \'sold\' or \'available\'')

def get_artwork_title():
    
    title = input('Enter artwork title: ') #Take title input
    return title

#Print artworks
def show_artwork(artworks):

    if artworks:
        print('')
        for artwork in artworks:
            print(artwork)
        print('')
    else:
        print('No artwork to display.')

def message(msg):
    print(msg)
from artstore import Artist, Artwork, ArtistDB, ArtworkDB, ArtstoreError
from menu import Menu
import ui

artist_log = ArtistDB()
artwork_log = ArtworkDB()

def main():
    
    menu = create_menu()

    while True:
        command = ui.get_choice(menu)
        action = menu.get_action(command)
        action()
        if command == 'Q':
            break

def create_menu():
    menu = Menu()
    menu.add_command('1', 'Add artist', add_artist)
    menu.add_command('2', 'Search for artwork by artist', search_artist)
    menu.add_command('3', 'Display available artwork by artist', display_artwork)
    menu.add_command('4', 'Add new artwork', add_artwork)
    menu.add_command('5', 'Delete artwork', delete_artwork)
    menu.add_command('6', 'Change artwork availability', change_availability)
    menu.add_command('Q', 'Quit', quit_program)

    return menu

def add_artist():
    #try:
        new_artist = ui.get_artist_info()
        new_artist.save()
    #except:
        #print('Sorry, you cannot add the same artist twice.')

"""Consider combining search_artist and display"""
def search_artist():
    first_name, last_name = ui.artist_match()
    match = artist_log.artist_search(first_name, last_name)
    artworks = artwork_log.artwork_by_artist(match)
    ui.show_artwork(artworks)

def display_artwork():
    first_name, last_name = ui.artist_match()
    match = artist_log.artist_search(first_name, last_name)
    artworks = artwork_log.artwork_by_artist(match)
    for artwork in artworks:
        if artwork.availability == 'sold':
            artworks.remove(artwork)
    ui.show_artwork(artworks)

"""Consider combining add artist and artwork"""
def add_artwork():
    #try:
        new_artwork, first_name, last_name = ui.get_artwork_info()
        new_artwork.save(first_name, last_name)
    #except:
        #print('Sorry, you cannot add the same artwork twice.')

def delete_artwork():
    del_artwork = ui.artwork_match()
    del_artwork.delete()

def change_availability():
    title = ui.artwork_match()
    artwork = artwork_log.artwork_search(title)
    new_available = ui.get_sale_info()
    artwork.available = new_available
    artwork.save()

def quit_program():
    print('Thanks!')

if __name__ == '__main__':
    main()
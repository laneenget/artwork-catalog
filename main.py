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
        action(command)
        if command == 'Q':
            break

def create_menu():
    menu = Menu()
    menu.add_command('1', 'Add artist', add_data)
    menu.add_command('2', 'Search for artwork by artist', search_and_display)
    menu.add_command('3', 'Display available artwork by artist', search_and_display)
    menu.add_command('4', 'Add new artwork', add_data)
    menu.add_command('5', 'Delete artwork', delete_artwork)
    menu.add_command('6', 'Change artwork availability', change_availability)
    menu.add_command('Q', 'Quit', quit_program)

    return menu

def add_data(command):
    first_name, last_name = ui.get_artist_name()
    artist_id = artist_log.artist_search(first_name, last_name)
    if artist_id == -1:
        if command == 1:
            new_artist = ui.get_artist_info(first_name, last_name)
            new_artist.save()
        elif command == 4:
            title = ui.get_artwork_title()
            new_artwork = ui.get_artwork_info(artist_id, title)
            new_artwork.save()

def search_and_display(command):
    first_name, last_name = ui.get_artist_name()
    id_match = artist_log.artist_search(first_name, last_name)
    artworks = artwork_log.artwork_by_artist(id_match)
    if command == 2:
        ui.show_artwork(artworks)
    elif command == 3:
        for artwork in artworks:
            if artwork.available == 'sold':
                artworks.remove(artwork)
            ui.show_artwork(artworks)
   
def delete_artwork(command):
    del_artwork = artwork_match()
    del_artwork.delete()

def change_availability(command):
    artwork = artwork_match()
    new_available = ui.get_sale_info()
    artwork.available = new_available
    artwork.update()

def artwork_match():
    title = ui.get_artwork_title()

    if artwork_log.artwork_search(title) != None:
        artwork = artwork_log.artwork_search(title)
        return artwork
    else:
        print('That artwork is not in the database.')

def quit_program():
    print('Thanks!')

if __name__ == '__main__':
    main()
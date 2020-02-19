from artstore import Artist, Artwork, ArtistDB, ArtworkDB, ArtstoreError
from menu import Menu
import ui

artist_log = ArtistDB()
artwork_log = ArtworkDB()

def main():
    
    menu = create_menu()

    while True:
        command = ui.get_choice(menu) #Get appropriate command
        action = menu.get_action(command) #Call action
        action()
        if command == 'Q': #End program
            break

#Add menu with list of commands
def create_menu():
    menu = Menu()
    menu.add_command('1', 'Add artist', add_artist)
    menu.add_command('2', 'Search for artwork by artist', search_by_artist)
    menu.add_command('3', 'Display available artwork by artist', search_by_artist_available)
    menu.add_command('4', 'Add new artwork', add_artwork)
    menu.add_command('5', 'Delete artwork', delete_artwork)
    menu.add_command('6', 'Change artwork availability', change_availability)
    menu.add_command('Q', 'Quit', quit_program)

    return menu

def add_artist():
    first_name, last_name = ui.get_artist_name() #Get artist first and last name
    artist_id = artist_log.artist_search(first_name, last_name) #Check to see if artist is already in the database
    if artist_id == -1:
        new_artist = ui.get_artist_info(first_name, last_name) #Create artist object
        new_artist.save() #Save artist to db
    else:
         ui.message('That artist is already in the database.')

def add_artwork():
    first_name, last_name = ui.get_artist_name() #Get artist first and last
    artist_id = artist_log.artist_search(first_name, last_name) #Get artist id
    if artist_id != -1:
        title = ui.get_artwork_title() #Get artwork title
        new_artwork = ui.get_artwork_info(artist_id, title) #Get other artwork info and create artwork object
        new_artwork.save() #Save artwork
    else:
        ui.message('Add the artist to the database first.')

#Returns artist works in a list
def search_and_display():
    first_name, last_name = ui.get_artist_name() #Get artist info
    id_match = artist_log.artist_search(first_name, last_name)
    artworks = artwork_log.artwork_by_artist(id_match) #Search database for artworks

    return artworks

def search_by_artist():
    artworks = search_and_display() #Call search_and_display for artworks list
    ui.show_artwork(artworks) #Show all

def search_by_artist_available():
    artworks = search_and_display() #Call search_and_display for artworks list
    for artwork in artworks:
        if artwork.available == 1:
            artworks.remove(artwork) #Remove any artwork that is not available
    ui.show_artwork(artworks) #Show available artwokrs
   
def delete_artwork():
    del_artwork = artwork_match() #Get artwork object
    del_artwork.delete() #Delete

def change_availability():
    artwork = artwork_match() #Get artwork object
    new_available = ui.get_sale_info() #Get new available info
    artwork.available = new_available #Change object availability
    artwork.update() #Update in db

def artwork_match():
    title = ui.get_artwork_title() #Get artwork title

    if artwork_log.artwork_search(title) != None:
        artwork = artwork_log.artwork_search(title) #Search for artwork
        return artwork
    else:
        ui.message('That artwork is not in the database.')

def quit_program():
    ui.message('Thanks!')

if __name__ == '__main__':
    main()
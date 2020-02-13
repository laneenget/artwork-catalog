from menu import Menu

def main():
    
    menu = create_menu()

def create_menu():
    menu = Menu()
    menu.add_command('1', 'Add artist', add_artist())
    menu.add_command('2', 'Search for artwork by artist', search_artist())
    menu.add_command('3', 'Display available artwork by artist', display_art())
    menu.add_command('4', 'Add new artwork', add_artwork())
    menu.add_command('5', 'Delete artwork', delete_artwork())
    menu.add_command('6', 'Change artwork availability', change_availability())

def add_artist():

def search_artist():

def display_artwork():

def add_artwork():

def delete_artwork():

def change_availability():


def get_choice():
    while True:
        command = input('Enter a key: ').upper()
        if is_valid(command):
            return command
        else:
            print('Not a valid choice, try again.')

def is_valid():


#def show_artwork():

#def get_artwork_id():

#def get_sale_info():
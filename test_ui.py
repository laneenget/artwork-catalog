from unittest import TestCase
from unittest.mock import patch
import os 

import artstore
from artstore import Artist, Artwork, ArtistDB, ArtworkDB

import ui
from menu import Menu

class TestUI(TestCase):

    @classmethod
    def setUp(cls):
        artstore.db = os.path.join('database', 'test_artstore.db')
        ArtistDB.instance = None 
        ArtworkDB.isntance = None

    @patch('builtins.input', side_effect=['a'])
    @patch('builtins.print')
    def test_get_choice(self, mock_print, mock_input):
        menu = Menu()

        menu.add_command('a', 'aaa', lambda: None)
        menu.add_command('b', 'bbb', lambda: None)

        self.assertEqual('a', ui.get_choice(menu))

        mock_print.assert_any_call(menu)

    @patch('builtins.input', side_effect=['first_name', 'last_name', 'email'])
    def test_get_artist_info(self, mock_input):
        artist = ui.get_artist_info()
        self.assertEqual('first_name', artist.first_name)
        self.assertEqual('last_name', artist.last_name)
        self.assertEqual('email', artist.email)

    @patch('builtins.input', side_effect=['first_name', 'last_name', 'title', 'price', 'available'])
    def test_get_artwork_info(self, mock_input):
        artwork = ui.get_artwork_info()
        self.assertEqual('title', artwork.title)
        self.assertEqual('price', artwork.price)
        self.assertEqual('available', artwork.available)

    @patch('builtins.input', side_effect=['available'])
    def test_get_sale_info(self, mock_input):
        sale_info = ui.get_sale_info()
        self.assertIn('available', sale_info)

    @patch('builtins.input', side_effect=['1234', 'puppy', 'BaNaNa', '-283.42'])
    def test_get_sale_info_invalid_input(self, mock_input):
        sale_info = ui.get_sale_info()
        self.assertIn('available', sale_info)

    @patch('builtins.input', side_effect=['first_name', 'last_name'])
    def test_artist_match(self, mock_input):
        first_name, last_name = ui.artist_match()
        self.assertIn('first_name', first_name)
        self.assertIn('last_name', last_name)

    @patch('builtins.input', side_effect=['title'])
    def test_artwork_match(self, mock_input):
        title = ui.artwork_match()
        self.assertIn('title', title)

    @patch('builtins.print')
    def test_show_books_list(self, mock_print):
        artwork1 = Artwork('title', 100.23, 'available', 1)
        artwork2 = Artwork('title2', 110.21, 'sold', 1)

        artworks = [artwork1, artwork2]

        ui.show_artwork(artworks)

        mock_print.assert_any_call(artwork1)
        mock_print.assert_any_call(artwork2)
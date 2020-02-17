from unittest import TestCase
import os

import artstore
from artstore import Artist, ArtistDB

class TestArtist(TestCase):

    @classmethod
    def setUp(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtistDB.instance = None

    def test_string(self):
        artist = Artist('artist1', 'artist1last', 'artist@email.com')
        self.assertIn('artist1', str(artist))
        self.assertIn('artist1last', str(artist))
        self.assertIn('artist@email.com', str(artist))

    def test_save(self):
        artist = Artist('artist1', 'artist1last', 'artist@email.com')
        artist.save()
        self.assertIsNotNone(artist.id)
        db = ArtistDB()
        self.assertTrue(db.artist_search(artist.first_name, artist.last_name))

class TestArtwork(TestCase):

    @classmethod
    def setUp(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtworkDB.instance = None

    def test_string(self):
        
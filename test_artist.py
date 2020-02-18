from unittest import TestCase
import os

import artstore
from artstore import Artist, ArtistDB, Artwork, ArtworkDB

class TestArtist(TestCase):

    @classmethod
    def setUp(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtistDB.instance = None

    def test_save(self):
        artist = Artist('artist1', 'artist1last', 'artist@email.com')
        artist.save()
        
        db = ArtistDB()
        self.assertTrue(db.artist_search(artist.first_name, artist.last_name))

class TestArtwork(TestCase):

    @classmethod
    def setUp(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtworkDB.instance = None

    def test_save(self):
        artwork = Artwork(1, 'testartwork', 220192.30, 'available')
        artwork.save()
        db = ArtworkDB()
        self.assertTrue(db.artwork_search(artwork.title))

    def test_update(self):
        artwork = Artwork(1, 'testartwork', 22029384.12, 'available')
        artwork.save()

        artwork.available = 'sold'
        artwork.update()

        db = ArtworkDB()

        self.assertEqual(artwork, db.artwork_search(artwork.title))

    def test_delete(self):
        artwork = Artwork(1, 'testartwork', 3274883.12, 'sold')
        artwork.save()

        artwork.delete()

        db = ArtworkDB()

        self.assertIsNone(db.artwork_search(artwork.title))

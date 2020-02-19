from unittest import TestCase
import os 

import artstore
from artstore import Artist, Artwork, ArtistDB, ArtworkDB, ArtstoreError

class TestArtistDB(TestCase):

    @classmethod
    def setUpClass(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtistDB.instance = None

    def setUp(self):
        self.adb = ArtistDB()
        self.clear_artistdb()

    def clear_artistdb(self):
        self.adb.delete_artists()

    def add_data(self):
        self.clear_artistdb()

        self.a1 = Artist('Art', 'Artiste', 'art@email.com')
        self.a2 = Artist('Artina', 'Potter', 'artina@email.com')
        self.a3 = Artist('Scully', 'Sculptor', 'scull@email.com')

        self.a1.save()
        self.a2.save()
        self.a3.save()

    def test_add_data(self):
        self.add_data()

        self.assertTrue(self.adb.artist_search(self.a1.first_name, self.a1.last_name))
        self.assertTrue(self.adb.artist_search(self.a2.first_name, self.a2.last_name))
        self.assertTrue(self.adb.artist_search(self.a3.first_name, self.a3.last_name))

    def test_search_artist(self):
        self.add_data()

        self.assertIsNotNone(self.adb.artist_search(self.a1.first_name, self.a1.last_name))

    def test_search_artist_not_found(self):
        self.add_data()

        self.assertIsNone(self.adb.artist_search('No artist', 'No artist'))

    def test_add_duplicate(self):
        self.add_data()

        with self.assertRaises(ArtstoreError):
            artist_dup = Artist('Art', 'Artiste', 'art@email.org')
            artist_dup.save()

class TestArtworkDB(TestCase):

    @classmethod
    def setUpClass(cls):
        artstore.db = os.path.join('test_artstore.db')
        ArtworkDB.instance = None
        ArtistDB.instance = None

    def setUp(self):
        self.awdb = ArtworkDB()
        self.adb = ArtistDB()
        self.clear_artwork_db()

    def clear_artwork_db(self):
        self.awdb.delete_all_artworks()
        self.adb.delete_artists()

    def add_data(self):
        self.clear_artwork_db()

        self.a1 = Artist('firstname', 'lastname', 'email')
        self.a2 = Artist('firstname1', 'lastname1', 'email1')

        self.a1 = Artwork(1, 'title1', 200.2, 'available')
        self.a2 = Artwork(1, 'title2', 20039471.21, 'sold')
        self.a3 = Artwork(2, 'title3', 2384789234.32, 'available')

        self.a1.save()
        self.a2.save()
        self.a3.save()

    def test_add_data(self):
        self.add_data()

        self.assertTrue(self.awdb.artwork_search(self.a1.title))
        self.assertTrue(self.awdb.artwork_search(self.a2.title))
        self.assertTrue(self.awdb.artwork_search(self.a3.title))

    def test_delete_data(self):
        self.add_data()

        self.a3.delete()
        self.assertIsNone(self.awdb.artwork_search(self.a3.title))

    def test_update_data(self):
        self.add_data()

        self.a1.available = 'sold'
        self.a1.update()
        
        a1_from_store = self.awdb.artwork_search(self.a1.title)
        self.assertTrue(a1_from_store.available)

    def test_add_duplicate(self):
        self.add_data()

        with self.assertRaises(ArtstoreError):
            artwork_dup = Artwork(1, 'title1', 200.2, 'available')
            artwork_dup.save()

    def test_artwork_search(self):
        self.add_data()

        self.assertCountEqual(self.a1, self.awdb.artwork_search(self.a1.title))

    def test_artwork_search_none(self):
        self.add_data()

        self.assertIsNone(self.awdb.artwork_search('No title'))

    def test_artwork_by_artist(self):
        self.add_data()

        self.assertCountEqual([self.a1, self.a2], self.awdb.artwork_by_artist)
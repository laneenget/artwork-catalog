import sqlite3
import os

db = os.path.join('catalog.db')

class Artist:

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

class ArtistDB:

    class _ArtistDB:

        def __init__():
            create_artist_tbl = 'CREATE TABLE IF NOT EXISTS artist (firstname TEXT, lastname TEXT, email TEXT, UNIQUE(firstname COLLATE NOCASE, lastname COLLATE NOCASE, email COLLATE NOCASE))'
            create_artwork_tbl = 'CREATE TABLE IF NOT EXISTS artwork (artist TEXT, title TEXT, price DECIMAL(10, 2), available BOOLEAN UNIQUE(title COLLATE NOCASE))'
        
            con = sqlite3.connect(db)
        
            with con:
                con.execute(create_artist_tbl)
                con.execute(create_artwork_tbl)

            con.close()

        def _add_artist():
            insert_artist = 'INSERT INTO artist (firstname, lastname, email) VALUES (?, ?, ?)'

            try: 
                with sqlite3.connect(db) as con:
                    row = con.execute(insert_artist, (artist.first_name, artist.last_name, artist.email) )
                    new_id = row.lastrowid  
                    artist.id = new_id  
            except sqlite3.IntegrityError as e:
                raise BookError(f'This artist is already in the database: {artist.first_name} {artist.last_name}')
            finally:
                con.close()

class Artwork:

class ArtworkDB:

    class _ArtworkDB:
        def __init__():

        def _add_artwork():

        def _delete_artwork():

        def _update_artwork():

import sqlite3
import os

db = os.path.join('catalog.db')
con = sqlite3.connect(db)
con.execute('PRAGMA foreign_keys = ON;')
con.close()

class Artist:

    def __init__(self, firstname, lastname, email, id = None):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id

        self.artistdb = ArtistDB()

    def save(self):

        self.artistdb._add_artist(self)
    

class ArtistDB:

    class _ArtistDB:

        def __init__(self):

            create_artist_tbl = 'CREATE TABLE IF NOT EXISTS artist (artist_id INT, firstname TEXT, lastname TEXT, email TEXT, UNIQUE(firstname COLLATE NOCASE, lastname COLLATE NOCASE, email COLLATE NOCASE), PRIMARY KEY(artist_id))'
        
            con = sqlite3.connect(db)
        
            with con:
                con.execute(create_artist_tbl)

            con.close()

        def _add_artist(self, artist):

            insert_artist = 'INSERT INTO artist (firstname, lastname, email) VALUES (?, ?, ?, ?)'

            try: 
                with sqlite3.connect(db) as con:
                    row = con.execute(insert_artist, (artist.first_name, artist.last_name, artist.email))
                    new_id = row.lastrowid  
                    artist.id = new_id  
            except sqlite3.IntegrityError as e:
                raise ArtstoreError(f'This artist is already in the database: {artist.first_name} {artist.last_name}')
            finally:
                con.close()

        def artist_search(self, artist):

            search_sql = 'SELECT rowid, * FROM artist WHERE UPPER(firstname) = UPPER(?) AND UPPER(lastname) = UPPER(?)'

            con = sqlite3.connect(db) 
            con.row_factory = sqlite3.Row 
            row = con.execute(search_sql, (artist.first_name, artist.last_name))
            result = row.fetchone()

            if result:
                artist = Artist(result['artist_id'], result['firstname'], result['lastname'], result['email'])
            else:
                artist = "None"
            con.close()

            return artist

class Artwork:

    def __init__(self, title, price, available, artist_id, id = None):

        self.title = title
        self.price = price
        self.available = available
        self.artist_id = artist_id
        self.id = id

        self.artworkdb = ArtworkDB()

    def save(self):

        if self.id:
            self.artworkdb._update_artwork(self)
        else:
            self.artworkdb._add_artwork(self)

    def delete(self):

        self.artworkdb._delete_artwork(self)

class ArtworkDB:

    class _ArtworkDB:

        def __init__(self):

            create_artwork_tbl = 'CREATE TABLE IF NOT EXISTS artwork (artwork_id INT, artist_id INT, title TEXT, price DECIMAL(10, 2), available BOOLEAN UNIQUE(title COLLATE NOCASE), PRIMARY KEY (artwork_id), FOREIGN KEY(artist_id) REFERENCES artist(artist_id))'

            con = sqlite3.connect(db)
        
            with con:
                con.execute(create_artwork_tbl)

            con.close()

        def _add_artwork(self, artwork):
            """Need a way to get artist id from artist table"""

            artist_id_query = 'SELECT id FROM artists WHERE firstname = ? and lastname = ?'
            insert_artwork_query = 'INSERT INTO artwork (?, ?, ?, ?, ?)'

            con = sqlite3.connect(db)

            with con:
                row = con.execute(artist_id_query)
                artist_id = row.fetchone()
                con.execute(insert_artwork_query, (artwork.id, artist_id, artwork.title, artwork.price, artwork.available))

            con.close()

        def _delete_artwork(self, artwork):

            delete_artwork_query = 'DELETE FROM artwork WHERE title = ?'

            con = sqlite3.connect(db)

            with con:
                con.execute(delete_artwork_query, (artwork.title))

            con.close()

        def _update_artwork(self, artwork):

            update_artwork_query = 'UPDATE artwork SET available = ? WHERE title = ?'

            con = sqlite3.connect(db)

            with con:
                con.execute(update_artwork_query, (artwork.available, artwork.title))

            con.close()

        def artwork_search(self, artwork):
            """Not sure about this one"""

            search_sql = 'SELECT rowid, * FROM artwork WHERE UPPER(title) = UPPER(?)'

            con = sqlite3.connect(db) 
            con.row_factory = sqlite3.Row 
            row = con.execute(search_sql, (artwork.title))
            result = row.fetchone()

            if result:
                artwork = Artwork(result['artwork_id'], result['artist_id'], result['title'], result['price'], result['available'])
            else:
                artwork = "None"
            con.close()

            return artwork

class ArtstoreError(Exception):
    pass
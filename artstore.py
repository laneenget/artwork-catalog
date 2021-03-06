import sqlite3
import os

db = os.path.join('catalog.db')
con = sqlite3.connect(db)
con.execute('PRAGMA foreign_keys = ON;')
con.close()

class Artist:

    def __init__(self, first_name, last_name, email, id = None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id

        self.artistdb = ArtistDB()

    def __str__(self):

        return 'Artist(firstname='+self.first_name+', lastname='+self.last_name+', email='+self.email+ ')'

    def __repr__(self):

        return {'firstname':self.first_name, 'lastname':self.last_name, 'email':self.email}

    def save(self):

        self.artistdb._add_artist(self)
    

class ArtistDB:

    def __init__(self):

        create_artist_tbl = 'CREATE TABLE IF NOT EXISTS artist (artistId INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT, UNIQUE(firstname COLLATE NOCASE, lastname COLLATE NOCASE, email COLLATE NOCASE))'
        
        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_artist_tbl)

        con.close()

    def _add_artist(self, artist):

        insert_artist = 'INSERT INTO artist (firstname, lastname, email) VALUES (?, ?, ?)'

        try: 
            with sqlite3.connect(db) as con:
                row = con.execute(insert_artist, (artist.first_name, artist.last_name, artist.email))
        except sqlite3.IntegrityError as e:
            raise ArtstoreError(f'This artist is already in the database: {artist.first_name} {artist.last_name}')
        finally:
            con.close()

    """Delete all artists from db for testing purposes"""
    def delete_artists(self):

        remove_artists = 'DELETE FROM Artist'

        con = sqlite3.connect(db)

        with con:
            con.execute(remove_artists)

        con.close()

    """Query database to find given artist"""
    def artist_search(self, first_name, last_name):

        search_sql = 'SELECT artistId FROM artist WHERE UPPER(firstname) = UPPER(?) AND UPPER(lastname) = UPPER(?)'

        con = sqlite3.connect(db) 
        con.row_factory = sqlite3.Row 
        row = con.execute(search_sql, (first_name, last_name))
        result = row.fetchone()

        if result:
            artist_id = int(result[0])
        else:
            artist_id = -1

        con.close()

        return artist_id

class Artwork:

    def __init__(self, title, price, available, artist_id, id = None):

        self.title = title
        self.price = price
        self.available = available
        self.artist_id = artist_id
        self.id = id

        self.artworkdb = ArtworkDB()

    def __str__(self):

        return self.title + ' ' + str(self.price)

    def __repr__(self):
        
        return {'title':self.title, 'price':str(self.price)}

    def save(self):

        self.artworkdb._add_artwork(self)

    def update(self):

        self.artworkdb._update_artwork(self)

    def delete(self):

        self.artworkdb._delete_artwork(self)

class ArtworkDB:

    instance = None

    def __init__(self):

        create_artwork_tbl = 'CREATE TABLE IF NOT EXISTS artwork (artist_id INT, title TEXT, price DECIMAL(10, 2), available INTEGER, FOREIGN KEY(artist_id) REFERENCES artist(rowid))'

        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_artwork_tbl)

        con.close()

    def _add_artwork(self, artwork):

        insert_artwork = 'INSERT INTO artwork (artist_id, title, price, available) VALUES (?, ?, ?, ?)'

        try: 
            with sqlite3.connect(db) as con:
                row = con.execute(insert_artwork, (artwork.artist_id, artwork.title, artwork.price, artwork.available))
        except sqlite3.IntegrityError as e:
            raise ArtstoreError(f'This artwork is already in the database: {artwork.title}')
        finally:
            con.close()

    def _delete_artwork(self, artwork):

        delete_artwork_query = 'DELETE FROM artwork WHERE title = ?'

        con = sqlite3.connect(db)

        with con:
            con.execute(delete_artwork_query, (artwork.title, ))

        con.close()

    """Delete all artworks from db for testing purposes"""
    def delete_all_artworks(self):

        remove_artworks = 'DELETE FROM Artwork'

        con = sqlite3.connect(db)

        with con:
            con.execute(remove_artworks)

        con.close()

    def _update_artwork(self, artwork):

        update_artwork_query = 'UPDATE artwork SET available = ? WHERE title = ?'

        con = sqlite3.connect(db)

        with con:
            con.execute(update_artwork_query, (artwork.available, artwork.title))

        con.close()

    """Query database to find row with given artwork title"""
    def artwork_search(self, title):

        search_sql = 'SELECT rowid, * FROM artwork WHERE UPPER(title) = UPPER(?)'

        con = sqlite3.connect(db) 
        con.row_factory = sqlite3.Row 
        row = con.execute(search_sql, (str(title), ))
        result = row.fetchone()

        if result:
            artwork = Artwork(result['title'], result['price'], result['available'], result['artist_id'])
        else:
            artwork = None
        con.close()

        return artwork

    """Query database to find all artwork by artist"""
    def artwork_by_artist(self, artist_id):

        artworks = []
        search_sql = 'SELECT * FROM artwork WHERE artist_id = ?'

        con = sqlite3.connect(db)

        con.row_factory = sqlite3.Row
        rows = con.execute(search_sql, (artist_id,))

        for r in rows:
            artwork = Artwork(r['title'], r['price'], r['available'], r['artist_id'])
            artworks.append(artwork)

        con.close()

        return artworks


class ArtstoreError(Exception):
    pass
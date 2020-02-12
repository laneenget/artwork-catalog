import sqlite3
import os

db = os.path.join('catalog.db')

class Art:

class ArtStore:

    class _ArtStore:

        def __init__():
            create_artist_tbl = 'CREATE TABLE IF NOT EXISTS artist (artist TEXT, email TEXT, UNIQUE(artist COLLATE NOCASE, email COLLATE NOCASE))'
            create_artwork_tbl = 'CREATE TABLE IF NOT EXISTS artwork (artist TEXT, title TEXT, price DECIMAL(10, 2), available BOOLEAN UNIQUE(title COLLATE NOCASE))'
        
            con = sqlite3.connect(db)
        
            with con:
                con.execute(create_artist_tbl)
                con.execute(create_artwork_tbl)

            con.close()

        def _add_artist():

        def _add_artwork():

        def _delete_artwork():

        def _update_artwork():

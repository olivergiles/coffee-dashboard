import os
import pathlib
import sqlite3
import streamlit as st

from app.cache import Cache
from app.constants import Constants

__all__ = ["CoffeeDB"]

class CoffeeDB:
    """Class to connect to the db.
    """
    def __init__(self) -> None:
        """Initilise the path to the db.
        """
        cache = Cache()
        self.path = cache.get_value_for_key(Constants.SELECTED_DATABASE)
        if self.path is None:
            base_path = pathlib.Path(__file__).resolve(
                ).parent.parent.joinpath("data", "coffee.db")
            Cache().cache_key_value(Constants.SELECTED_DATABASE, str(base_path))
            self.path = str(base_path)

    @st.experimental_singleton
    def get_cursor(_self) -> sqlite3.Cursor:
        """Return the cursor for the db.

        Returns:
            sqlite3.Cursor: Cursor object connected to the db.
        """
        connection = sqlite3.connect(_self.path, check_same_thread=False)
        cursor = connection.cursor()
        return cursor

    @st.experimental_singleton
    def get_connection(_self) -> sqlite3.Connection:
        """Return a connection to the db.

        Returns:
            sqlite3.Connection: Connection object connected to the db.
        """
        connection = sqlite3.connect(_self.path, check_same_thread=False)
        return connection

if __name__ == "__main__":
    query = CoffeeDB().get_cursor().execute("""
            SELECT *
            FROM merged_data_cleaned
            LIMIT 10
    """)
    for item in query:
        print(item)

import os
import pathlib
import sqlite3
import streamlit as st

from app.cache import Cache
from app.constants import Constants

__all__ = ["CoffeeDB"]

class CoffeeDB:
    """
    _summary_
    """
    def __init__(self) -> None:
        cache = Cache()
        self.path = cache.get_value_for_key(Constants.SELECTED_DATABASE)
        if self.path is None:
            base_path = pathlib.Path(__file__).resolve(
                ).parent.parent.joinpath("data", "coffee.db")
            Cache().cache_key_value(Constants.SELECTED_DATABASE, str(base_path))
            self.path = str(base_path)

    @st.experimental_singleton
    def get_cursor(_self):
        connection = sqlite3.connect(_self.path, check_same_thread=False)
        cursor = connection.cursor()
        return cursor

if __name__ == "__main__":
    query = CoffeeDB().get_cursor().execute("""
            SELECT *
            FROM merged_data_cleaned
            LIMIT 10
    """)
    for item in query:
        print(item)

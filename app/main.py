import pandas as pd
import streamlit as st

from app.database import CoffeeDB

class Dashboard():
    def __init__(self) -> None:
        self.db = CoffeeDB()

    def title(self) -> None:
        st.title("Coffee Quality Dashboard!")

    def body(self) -> None:
        connection = self.db.get_connection()
        test_query = pd.read_sql_query("SELECT * FROM merged_data_cleaned",
                                       connection, index_col='')
        st.dataframe(test_query)

    def render(self) -> None:
        self.title()
        self.body()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.render()

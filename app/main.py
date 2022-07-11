import pandas as pd
import streamlit as st

from app.database import CoffeeDB

class Dashboard():
    def __init__(self) -> None:
        """Init the dashboard class and the connection to the db
        """
        self.db = CoffeeDB()

    def title(self) -> None:
        """Generates the tile for the page
        """
        st.title("Coffee Quality Dashboard!")

    def body(self) -> None:
        """Generate the main body of the app.
        """
        connection = self.db.get_connection()
        test_query = pd.read_sql_query("SELECT * FROM merged_data_cleaned",
                                       connection, index_col='')
        st.write(test_query.columns)

    def render(self) -> None:
        """Render the dashboard
        """
        self.title()
        self.body()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.render()

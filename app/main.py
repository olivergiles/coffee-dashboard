import streamlit as st

class Dashboard():
    def __init__(self) -> None:
        pass

    def title(self) -> None:
        st.title("Coffee Quality Dashboard!")

    def render(self) -> None:
        self.title()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.render()

import streamlit as st

__all__ = ["Cache"]


class Cache:
    def cache_key_value(self, key, value):
        """_summary_

        Args:
            key (_type_): _description_
            value (_type_): _description_
        """
        st.session_state[key] = value

    def get_value_for_key(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return st.session_state.get(key, None)

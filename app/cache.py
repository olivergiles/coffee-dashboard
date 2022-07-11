from typing import Any
import streamlit as st

__all__ = ["Cache"]


class Cache:
    """Class for the streamlit cache object.
    """
    def cache_key_value(self, key: str, value: Any) -> None:
        """Function to cache a value in streamlit cache.

        Args:
            key (str): Key to cache value.
            value (Any): Value to cache.
        """
        st.session_state[key] = value

    def get_value_for_key(self, key: str) -> Any:
        """Get a value for a given key from streamlit cache.

        Args:
            key (str): Key to cache value.

        Returns:
            Any: The value for the given key from the
            cache or None if not in cache.
        """
        return st.session_state.get(key, None)

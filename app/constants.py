from enum import Enum

__all__ = ["Constants"]

class Constants(Enum):
    SELECTED_DATABASE = "selected database"

if __name__ == "__main__":
    print(Constants.SELECTED_DATABASE)

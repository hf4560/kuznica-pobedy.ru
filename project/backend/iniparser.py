import configparser
from urllib.parse import quote_plus

class Config(configparser.ConfigParser):
    def __init__(self, path: str):
        super().__init__()
        self.read(path)

    def getValue(self, section: str, key: str):
        try:
            return quote_plus(self[section][key])
        except Exception as e:
            raise e
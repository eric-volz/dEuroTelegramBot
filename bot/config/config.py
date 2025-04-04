import configparser


class Config(object):

    def __init__(self):
        self.parser = configparser.ConfigParser()

    def init(self, path: str) -> None:
        self.parser.read(path)

    def get_value(self, section: str, key: str) -> str:
        return self.parser.get(section, key)

    def get_section(self, section: str) -> dict:
        return dict(self.parser[section])

    def get_sections(self) -> list:
        return self.parser.sections()


config = Config()
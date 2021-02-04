import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def get_home_page():
        return config.get('common data', 'home_page')

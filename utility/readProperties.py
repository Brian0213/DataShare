import configparser
import os

config = configparser.RawConfigParser()

# Get the absolute path to the current script (readProperties.py)
current_script_path = os.path.abspath(__file__)

# Get the directory containing readProperties.py
current_dir = os.path.dirname(current_script_path)

# Navigate up one level to project root, then to Configurations/config.ini
config_path = os.path.join(os.path.dirname(current_dir), 'Configurations', 'config.ini')

# Read the config file
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_fname():
        return config.get('USER', 'fname')

    @staticmethod
    def get_lname():
        return config.get('USER', 'lname')

    @staticmethod
    def get_email():
        return config.get('USER', 'email')

    @staticmethod
    def get_role():
        return config.get('USER', 'role')

import logging
import datetime
from os import path


class Logs:
    """
    The class whose methods can write in search.log file or read saved repo names from search.log file
    """

    @staticmethod
    def log_search(search_request):
        """This static method saves inputted data in search.log file"""
        date = datetime.datetime.now()
        logging.basicConfig(filename='search.log', level=logging.INFO, format=f'{date.strftime("%d/%m/%Y %H:%M")} -> %(message)s')
        logging.info(search_request)

    @staticmethod
    def print_searched_repos(file_name):
        """This static method reads data from search.log file and then prints"""
        if path.exists(file_name):  # Checks if file exits (created or not)
            with open(file_name) as f:
                f = f.readlines()
                for string in f:
                    print(string.strip())
        else:
            print('File does not exits')

import json


class ConfigLoader:

    @staticmethod
    def load_config(file_name):
        """
        :param file_name: A name of a json file that represents the
        configuration settings of the game
        :return: an object that holds the settings of the game
        """
        f = open(file_name)
        config = json.load(f)
        return config

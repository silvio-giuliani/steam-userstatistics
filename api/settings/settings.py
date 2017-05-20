import json
import os

ROOT_DIR = os.path.abspath('.')


class Settings:

    def __init__(self):
        environment = self.__get_environment()
        settings = self.__get_settings(environment)
        self.settings = settings

    def __get_environment(self):
        settings = json.load(open(os.path.join(ROOT_DIR, 'api/configs/environment.json')))
        env = settings['environment']
        return env

    def __get_settings(self, environment):
        if environment is None:
            raise ValueError('environment argument expected!')

        file_name = 'api/configs/settings-{0}.json'.format(environment)
        settings = json.load(open(os.path.join(ROOT_DIR, file_name)))
        return settings

#teste = Settings()

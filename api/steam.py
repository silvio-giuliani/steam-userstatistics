import requests
from api.settings import settings


class Steam:
    def __init__(self):
        self.config = settings.Settings()

    def __get_owned_games(self):
        steam_config = self.config.settings["steam"]
        steam_api_url = '{0}/IPlayerService/GetOwnedGames/v0001/?key={1}&steamid={2}&include_appinfo=1format=json'
        get = requests.get(steam_api_url.format(steam_config["api_url"], steam_config["key"], steam_config["steamid"]))
        return get

    def get_games_statistics(self):
        req = self.__get_owned_games()

        if not req.status_code == 200:
            raise ValueError('It was not possible to complete a steam request.')

        response_data = req.json()['response']

        if response_data is None:
            raise ValueError('No request data available.')

        filtered_list = self.__get_played_only_games(response_data["games"])

        return filtered_list

    def __get_played_only_games(self, game_list):
        filtered_list = []

        for game in game_list:
            if game["playtime_forever"] > 0:
                filtered_list.append(game)

        return filtered_list
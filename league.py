from dotenv import load_dotenv
import os
import requests
import league_constants

my_region = 'na1'


def fetch_champions_dict():
    try:
        response = requests.get(league_constants.CHAMPIONS_URL)
        if response.status_code == 200:
            champion_data = response.json()['data']
            champion_id_to_name = {}
            for champion_key, champion_info in champion_data.items():
                champion_id = champion_info['key']
                champion_name = champion_info['name']
                champion_id_to_name[champion_id] = champion_name
            return champion_id_to_name
        else:
            print(f'Failed to fetch champion data. Status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'An error occurred: {e}')


TEAM = {'100': 'Blue', '200': 'Red'}


class LeagueScraper:
    def __init__(self):
        load_dotenv()
        self.champions_dict = fetch_champions_dict()
        self.headers = {'X-Riot-Token': os.getenv("LEAGUE_API_KEY")}

    def get_summoner_id(self, summoner_name):
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['id']
        else:
            print("Error Getting Summoner:", response.status_code)
            return None

    # Function to get active game by summoner ID
    def get_active_game(self, summoner_id):
        url = f'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Summoner is not currently in a game.")
            return None
        else:
            print("Error:", response.status_code)
            return None

    def get_random_active_game(self):
        url = f'https://na1.api.riotgames.com/lol/spectator/v4/featured-games'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Summoner is not currently in a game.")
            return None
        else:
            print("Error:", response.status_code)
            return None

    def get_participants_from_game(self, active_game):
        format_participants = lambda participant: {
            'champion_name': self.champions_dict[str(participant['championId'])],
            'champion_id': participant['championId'],
            'summoner_name': participant['summonerName'],
            'summoner_id': participant['puuid'],
            'team': TEAM[str(participant['teamId'])]
        }
        return list(map(format_participants, active_game.get('participants')))


    def get_game_info(self, summoner_name):
        summoner_id = self.get_summoner_id(summoner_name)
        print(summoner_id)
        if not summoner_id:
            return None
        game = self.get_active_game(summoner_id)
        if not game:
            return None
        participants = self.get_participants_from_game(game)
        if not participants:
            return None

        return {
            'summoner_name': summoner_name,
            'participants': participants
        }


if __name__ == "__main__":
    league = LeagueScraper()
    print(league.get_game_info('cegnsl'))
    print(league.get_game_info('AD13'))
    print(league.get_game_info('Spica'))
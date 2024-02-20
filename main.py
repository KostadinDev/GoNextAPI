from typing import Union

from fastapi import FastAPI
from gpt import GPT
from league import LeagueScraper

dummy_game_info = {'summoner_name': 'cegnsl', 'participants': [{'champion_name': 'Vladimir', 'champion_id': 8, 'summoner_name': 'cegnsl', 'summoner_id': 'TW9UEETzoV7Bk6xI4gt0FT5ZHPxojz3pCCO8Vbf1dmiNmd50XfVlNjns98ry5rl77VDkd0mSrEJGEw', 'team': 'Blue'}, {'champion_name': 'Ziggs', 'champion_id': 115, 'summoner_name': 'lolurmomiscool', 'summoner_id': 'xi1mvG4KjCfAA6i4HjkOe7XTzr-vMZ2bsuIeZaADQWb_wLb5c0rAd-iibHSnfyiD4h7Yh2s4VW0e4g', 'team': 'Blue'}, {'champion_name': 'Vi', 'champion_id': 254, 'summoner_name': 'JòyBòÿ', 'summoner_id': 'bi0HYJXMDQc-S9eu4m09HBYWtwnpUSj8p-xJ1zhGBFqdoFm_n6PHhxI6mNwF0UqgZpUppJu2tNAGAg', 'team': 'Blue'}, {'champion_name': 'Veigar', 'champion_id': 45, 'summoner_name': 'Van1sheD', 'summoner_id': '3VwQh6l-W6Ac36nE6PTBsqh8M4N3LOWoox1FD5mNafpzlI2aWMVw9VRC0Dr6FmBXGNb3FcjqQnl_Xg', 'team': 'Blue'}, {'champion_name': 'Camille', 'champion_id': 164, 'summoner_name': 'Madlogic23', 'summoner_id': 'SsYzzScVxpL18nOqNoqoPHw_MHTi6en77b-K4DK0zp7UF7wbLzwP8KH2Z7atfKa1-9nwKhjJda6WzA', 'team': 'Blue'}, {'champion_name': 'Ezreal', 'champion_id': 81, 'summoner_name': 'Trolling Master', 'summoner_id': 'Bqebivcd7lxUcMVFumdbaiWGxMPNsPdfn9P1CIZcW0J1e55wi7lByzUl3brnjdPgPJfSys60H9oS3g', 'team': 'Red'}, {'champion_name': 'Tahm Kench', 'champion_id': 223, 'summoner_name': 'TEEEEMOL', 'summoner_id': 'Mzk8HmdzDJ6699hl6BWlcUVGrFGvEItRbWHGHMOItUNCvOMQyhyxKaCv5gP9AJJGRrdZuQx7g9C2cw', 'team': 'Red'}, {'champion_name': 'Samira', 'champion_id': 360, 'summoner_name': 'Jg Pls or Troll', 'summoner_id': 'jeJuWiKaO1lkhHqPNdxyuXxJrd51zQ1TU1Li-hr-KygRXJYPFgkm95JGT6HmWty44LsFlQh1Nkiv5A', 'team': 'Red'}, {'champion_name': 'Hwei', 'champion_id': 910, 'summoner_name': 'Only Jesus Saves', 'summoner_id': 'MhspV67tGK86rOwugZW_X_9Fve7x2_MrMRyLI2yKelXXZBdlu4w08Bng4xdttz3VRu35_isgF3btKA', 'team': 'Red'}, {'champion_name': 'Yasuo', 'champion_id': 157, 'summoner_name': 'xDokusei', 'summoner_id': '4_QE4Ax_Vhn4V0USZzZJNTek5zqjiG520C6ZdHtLgKwkPa5wmsLuJ9ogCla9aAG6dpY40eysNC57mg', 'team': 'Red'}]};


app = FastAPI()

@app.get('/active-game/{region}/{user}')
def get_active_game(region: str, user: str, q: Union[str, None] = None):
    return {
        'game': dummy_game_info
    }

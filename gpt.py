from dotenv import load_dotenv
import os
from openai import OpenAI
from pprint import pprint

dummy_response = '''
Blue Team:
- Top Lane: Vladimir (cegnsl)
- Mid Lane: Ziggs (lolurmomiscool)
- Jungle: Vi (JòyBòÿ)
- ADC: Veigar (Van1sheD)
- Support: Camille (Madlogic23)

Red Team:
- Top Lane: Hwei (Only Jesus Saves)
- Mid Lane: Yasuo (xDokusei)
- Jungle: Ezreal (Trolling Master)
- ADC: Samira (Jg Pls or Troll)
- Support: Tahm Kench (TEEEEMOL)

Here is the advice for playing the champions and the overall game strategy:

1. Vladimir (Blue Top Lane):
- Vladimir is a strong scaling AP champion with sustain and high burst damage.
- Focus on farming and scaling to become a late-game threat.
- Use your Q ability (Transfusion) to poke and sustain in lane.
- Be cautious against Hwei's (Red Top Lane) all-ins, as his champion has high burst damage.
- Build items like Hextech Rocketbelt, Zhonya's Hourglass, and Rabadon's Deathcap for damage and survivability.

2. Ziggs (Blue Mid Lane):
- Ziggs is a long-range AP mage with wave clear and tower destruction capabilities.
- Use your Q ability (Bouncing Bomb) and W ability (Satchel Charge) to poke and control the wave.
- Roam and help your team secure objectives with your R ability (Mega Inferno Bomb).
- Be careful of all-ins from Yasuo (Red Mid Lane), as he can block your abilities with Wind Wall.
- Build items like Luden's Echo, Liandry's Anguish, and Zhonya's Hourglass for increased damage.

3. Vi (Blue Jungle):
- Vi is a bruiser-type champion with strong engage and damage.
- Focus on ganking and providing pressure in the lanes.
- Use your Q ability (Vault Breaker) and R ability (Assault and Battery) to lock down priority targets.
- Be mindful of Ezreal's (Red Jungle) mobility and Tahm Kench's (Red Support) ability to save allies.
- Build items like Trinity Force, Sterak's Gage, and Guardian Angel for damage and survivability.

4. Veigar (Blue ADC):
- Veigar is a mage-type ADC with high burst damage and crowd control.
- Farm and stack your passive (Phenomenal Evil Power) to increase your AP.
- Utilize your E ability (Event Horizon) to set up kills and protect yourself from engages.
- Be mindful of Samira's (Red ADC) mobility and Tahm Kench's (Red Support) ability to save allies.
- Build items like Luden's Echo, Hextech Rocketbelt, and Rabadon's Deathcap for increased burst damage.

5. Camille (Blue Support):
- Camille is an aggressive support with crowd control and engage potential.
- Zone and harass the enemy ADC in lane using your E ability (Hookshot) and Q ability (Precision Protocol).
- Coordinate with your ADC to engage and secure kills.
- Be cautious of Tahm Kench's (Red Support) ability to devour and save his ADC.
- Build items like Divine Sunderer, Sterak's Gage, and Guardian Angel for survivability and utility.

Game Plan:

- Early Game: Focus on farming and scaling in the laning phase. Coordinate with the Jungle (Vi) to secure objectives like Dragon and Rift Herald.
- Mid Game: Look for opportunities to roam and help other lanes. Prioritize objectives like Dragon and Towers. Use your wave clear and poke to control the map.
- Late Game: Group as a team and look to team fights. Utilize your champion's strengths and decide on the best targets for elimination. Coordinate with your team to secure Baron and push for the enemy base.

Remember to communicate with your team, ward important areas, and adapt to the match as it unfolds. Good luck in your game!
'''

class GPT:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GPT_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.model = 'gpt-3.5-turbo'
        self.max_tokens = 1000


    def ask_game_dummy(self, game_info):
        return dummy_response

    def ask_game(self, game_info):
        system_message = '''
        You are a live game league of legends assistant. Given an active game provided to you have to give advice on how to play the champion of the user and also provide advice on how to play
        the matchups in lane and jungle. Furthermore, take a look at the scaling of each team and advise a game plan for
        early game, mid game, and late game. Give helpful advise in terms of objectives, specific tips and tricks for the
        matchups, and item builds for the champion that will be best in this game.
        '''

        user_message = f'''
        Below is the game information and my summoner name. Please advise me about the current game.
        {str(game_info)}
        '''
        messages = [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message}
        ]
        # pprint(messages)
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens
        )
        return completion.choices[0].message.content


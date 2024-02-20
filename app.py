from flask import Flask, render_template_string
from league import LeagueScraper
from gpt import GPT

app = Flask(__name__)
gpt = GPT()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/active_game/<server>/<summoner_user>')
def get_active_game(server, summoner_user):
    league = LeagueScraper()
    game_info = league.get_game_info(summoner_user)
    if (game_info):
        advise = gpt.ask_game_dummy(game_info)
        return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pretty Format</title>
            <style>
                /* Style the container */
                .pretty-format {
                    white-space: pre-wrap; /* Preserve line breaks */
                    font-family: Arial, sans-serif; /* Choose a readable font */
                    font-size: 14px; /* Adjust font size as needed */
                    padding: 10px; /* Add padding for better readability */
                    border: 1px solid #ccc; /* Add a border for separation */
                    background-color: #f9f9f9; /* Add a light background color */
                    border-radius: 5px; /* Add some rounded corners */
                }
            </style>
        </head>
        <body>

        <!-- Place your long string inside a container with a class -->
        <div class="pretty-format">
            <!-- Your long string here -->
            {{ long_string }}
        </div>

        </body>
        </html>
        """,
        long_string=advise
    )
    else:
        return 'User not found!'

if __name__ == '__main__':
    app.run(debug=True)
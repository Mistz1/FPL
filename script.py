import requests
from collections import Counter

all_picks = [] # a variable to store the XI of all the top managers
Leaderboard_API = "https://fantasy.premierleague.com/api/leagues-classic/314/standings/"
PLAYER_API = "https://fantasy.premierleague.com/api/bootstrap-static/"
player_data = requests.get(PLAYER_API).json()["elements"] # a variable that stores all players name linked to their id to convert id to name

def get_latest_gameweek(): # gets the latest active gameweek
    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/") # stores the GET request from the API for all game weeks

    if response.status_code == 200: # checks if the site is available 
        data = response.json() # stores the response in json format
        current_gameweek = data["events"] # grabs the gameweek id
        latest_gameweek = None # prepare a variable for the latest gameweek
        for gw in current_gameweek: # loops through all the game weeks 
            if not gw["finished"]: # checks which game week is not finished
                latest_gameweek = gw["id"] # stores its id in the variable
                break
        return latest_gameweek # returns the variable 
    else:
        print("Failed to get data from the API") # if the process failed this tells us
        return None    
gameweek = get_latest_gameweek() # stores the output of the function above in a variable

# the code bellow will get the top managers ids 

response = requests.get(Leaderboard_API) # get request from the api
data = response.json() # converts it to json and stores it 

top_managers = data["standings"]["results"] # grabs the to managers and where they placed


def get_manager_squad(manager_id, gameweek): # a function to get all the squads from the top managers
    url = f"https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gameweek}/picks/" # the url for the API
    response = requests.get(url).json() # stores the result and converts it into json
    return response["picks"] # returns the squad

for manager in top_managers[:100]: # loops through top managers
    manager_id = manager["entry"] # gets their ID
    squad = get_manager_squad(manager_id, gameweek) # uses the function above to get the squad for each manager
    player_ids = [player["element"] for player in squad] # gets all the ids for the players
    all_picks.extend(player_ids) # appends the to a list


player_counts = Counter(all_picks) # counts how much a player was picked in a squad

def get_player_name(player_id): # a function to get the player name 
    for player in player_data: # loops through all the players
        if player["id"] == player_id: # finds the player id and pairs it with their name 
            return player["web_name"] # returns the player name
    return "Unknown player" # if the player wasnt found it returns unkown player

for player_id, count in player_counts.most_common(25): # loops through all the players
    print(f"{get_player_name(player_id)} - picked by {count} managers") # prints the most common one
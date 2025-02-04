# FPL Top Managers Squad Analyzer

This is my first ever project! 🎉

## About the Project
This script analyzes the most-picked players in Fantasy Premier League (FPL) by the top managers. It retrieves the squads of the top 100 managers from the official FPL API and counts how frequently each player is selected.

## Features
- Retrieves the latest active gameweek automatically
- Fetches the top managers from the FPL leaderboard
- Extracts player selections for the gameweek
- Counts and displays the most-picked players

## How It Works
1. Fetches the latest gameweek from the FPL API.
2. Retrieves the top 100 managers from the global leaderboard.
3. Fetches each manager's selected squad for the current gameweek.
4. Counts how many times each player appears.
5. Prints the top 25 most-picked players.

## Requirements
- Python 3
- `requests` library (install using `pip install requests`)

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/mistz1/FPL-Top-Managers-Squad-Analyzer.git
   ```
2. Navigate to the project folder:
   ```sh
   cd FPL-Top-Managers-Squad-Analyzer
   ```
3. Install dependencies:
   ```sh
   pip install requests
   ```
4. Run the script:
   ```sh
   python script.py
   ```

## Notes
- This project uses the official FPL API, which may change over time.
- The leaderboard ID used in the script is for the global league (ID 314). You can modify it to analyze a custom league.

## Future Improvements
- Add error handling for API failures.
- Improve efficiency of player name lookup.
- Create a web dashboard for visualization.

## Acknowledgments
This project is built using data from the [Fantasy Premier League](https://fantasy.premierleague.com/) API.

---
This is my first project, and I'm excited to improve it over time! 🚀


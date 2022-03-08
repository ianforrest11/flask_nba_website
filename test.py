import pandas as pd
import sqlite3
from datetime import datetime

# connect to database
conn = sqlite3.connect('test_database.db') 
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS pg_stats")

c.execute('''
CREATE TABLE pg_stats
AS
SELECT first_name AS "First Name", last_name AS "Last Name", team_abbr as "Team", age AS "Age", games_played AS "GP", games_started AS "GS",
ROUND(CAST(minutes AS float(1))/CAST(games_played AS float(1)), 1) AS "MPG",
ROUND(CAST(fgm AS float(1))/CAST(games_played AS float(1)), 1) AS "FGMPG",
ROUND(CAST(fga AS float(1))/CAST(games_played AS float(1)), 1) AS "FGAPG",
fg_pct AS "FG%",
ROUND(CAST(fg3m AS float(1))/CAST(games_played AS float(1)), 1) AS "3MPG",
ROUND(CAST(fg3a AS float(1))/CAST(games_played AS float(1)), 1) AS "3APG",
fg3_pct AS "3FG%",
ROUND(CAST(ftm AS float(1))/CAST(games_played AS float(1)), 1) AS "FTMPG", 
ROUND(CAST(fta AS float(1))/CAST(games_played AS float(1)), 1) AS "FTAPG",
ft_pct AS "FT%",
ROUND(CAST(points AS float(1))/CAST(games_played AS float(1)), 1) AS "PPG",
ROUND(CAST(orebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "ORPG",
ROUND(CAST(drebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "DRPG",
ROUND(CAST(rebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "RPG",
ROUND(CAST(assists AS float(1))/CAST(games_played AS float(1)), 1) AS "APG",
ROUND(CAST(steals AS float(1))/CAST(games_played AS float(1)), 1) AS "SPG",
ROUND(CAST(blocks AS float(1))/CAST(games_played AS float(1)), 1) AS "BPG", 
ROUND(CAST(turnovers AS float(1))/CAST(games_played AS float(1)), 1) AS "TPG",
ROUND(CAST(fouls AS float(1))/CAST(games_played AS float(1)), 1) AS "FPG" 
FROM player_stats_2122;''')
players_query = c.execute('''SELECT * FROM pg_stats''').fetchall()
for player in players_query:
    print(player)
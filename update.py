import sqlite3
from nba_api.stats.endpoints import playercareerstats, playergamelog
from nba_api.stats.static import players
import time

# get nba players
nba_players = players.get_players()
time.sleep(0.6)

# connect to database
conn = sqlite3.connect('test_database.db') 
c = conn.cursor()

# get number of rows in table
c.execute('''SELECT COUNT(*)
FROM player_stats_2122;''')
number_of_rows = c.fetchall()[0][0]
print('number of rows:', number_of_rows)

# query database row by row
for i in range(number_of_rows):
    # query existing data in the database
    c.execute('''SELECT * FROM player_stats_2122 LIMIT 1 OFFSET (?);''',(str(i),))
    row = c.fetchall()[0]
    # isolate player id to feed into PlayerCareerStatistics model

    nba_player_id = row[1]
    # isolate id to add to tuple
    id = row[0]
    # isolate name
    first_name = row[2]
    last_name = row[3]
    # isolate most recent stats
    most_recent_stats = playercareerstats.PlayerCareerStats(player_id=nba_player_id).get_data_frames()[0].iloc[-1]
    most_recent_stats = [x if (type(x) != float or x.is_integer() == False) else int(x) for x in list(most_recent_stats)]
    most_recent_stats.drop(['SEASON_ID','LEAGUE_ID'], inplace=True)
    print(most_recent_stats.index)
    print(most_recent_stats)

    print(most_recent_stats)
    print(row)
    most_recent_stats.insert(0,id)
    most_recent_stats.insert(2, first_name)
    most_recent_stats.insert(3,last_name)
    print(most_recent_stats)
    print('\n')    







    print('\n')
    time.sleep(0.6)

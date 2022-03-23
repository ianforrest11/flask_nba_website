import sqlite3
from nba_api.stats.endpoints import playercareerstats, playergamelog
from nba_api.stats.static import players
import time
from datetime import datetime
import sys


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

# get columns
c.execute('''PRAGMA table_info(player_stats_2122);''')
columns = [x[1] for x in c.fetchall()]

# get list of all player ids who are playing in 21-22 season and are currently in database
c.execute('''SELECT nba_player_id FROM player_stats_2122''')
nba_player_ids = [x[0] for x in c.fetchall()]

# iterate through players to check for ones not present in database
for player in nba_players:
    name = player['full_name']
    first_name = player['first_name']
    last_name = player['last_name']
    id = player['id']

    player_career_stats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()[0]
    
    # try to get most recent season for players
    try:
        most_recent_season = player_career_stats.iloc[-1]
    
    # exception if dataframe empty
    except:
        print(name, ' error')
        print(player_career_stats)
        print('\n')
        # end iteration of loop and move on to next person
        continue

    try:
        if most_recent_season['SEASON_ID'] == '2021-22' and id not in nba_player_ids:
            print(name, "not in database.  Adding...")
            print(most_recent_season)
            print('name:', name)
            print(name, 'is a current player')
            nba_player_id = int(most_recent_season['PLAYER_ID'])
            print('id:', id)
            nba_team_id = int(most_recent_season['TEAM_ID'])
            if nba_team_id == 0:
                nba_team_id = int(player_career_stats.iloc[-2]['TEAM_ID'])
            else:
                nba_team_id = int(most_recent_season['TEAM_ID'])
            print('nba_team_id:', nba_team_id)
            team_abbr = most_recent_season['TEAM_ABBREVIATION']
            if team_abbr == 'TOT':
                team_abbr = player_career_stats.iloc[-2]['TEAM_ABBREVIATION']
            else:
                team_abbr = most_recent_season['TEAM_ABBREVIATION']
            print('team_abbr:', team_abbr)
            # age
            age = int(most_recent_season['PLAYER_AGE'])
            print('age:', age)
            # games played
            games_played = int(most_recent_season['GP'])
            print('games_played:', games_played)
            # games started
            games_started = int(most_recent_season['GS'])
            print('games_started:', games_started)
            # minutes
            minutes = int(most_recent_season['MIN'])
            print('minutes:', minutes)
            # fgm
            fgm = int(most_recent_season['FGM'])
            print('fgm:', fgm)
            # fga
            fga = int(most_recent_season['FGA'])
            print('fga:', fga)
            # field goal %
            try:
                fg_pct = "%0.3f" % round(float(fgm/fga),3)
            except:
                fg_pct = "%0.3f" % round(float(0), 3)
            print('fg_pct:', fg_pct)
            # fg3m
            fg3m = int(most_recent_season['FG3M'])
            print('fg3m:', fg3m)
            # fg3a
            fg3a = int(most_recent_season['FG3A'])
            print('fg3a:', fg3a)
            # 3pt field goal %
            try:
                fg3_pct = "%0.3f" % round(float(fg3m/fg3a),3)
            except:
                fg3_pct = "%0.3f" % round(float(0), 3)
            print('fg3_pct:', fg3_pct)
            ftm = int(most_recent_season['FTM'])
            print('ftm:', fgm)
            fta = int(most_recent_season['FTA'])
            print('fta:', fta)
            ft_pct = float(most_recent_season['FT_PCT'])
            print('ft_pct:', ft_pct)
            points = int(most_recent_season['PTS'])
            print('points:', points)
            orebounds = int(most_recent_season['OREB'])
            print('orebounds:', orebounds)
            drebounds = int(most_recent_season['DREB'])
            print('drebounds:', drebounds)
            rebounds = int(most_recent_season['REB'])
            print('rebounds:', rebounds)
            assists = int(most_recent_season['AST'])
            print('assists:', assists)
            steals = int(most_recent_season['STL'])
            print('steals:', steals)
            blocks = int(most_recent_season['BLK'])
            print('blocks:', blocks)
            turnovers = int(most_recent_season['TOV'])
            print('turnovers:', turnovers)
            fouls = int(most_recent_season['PF'])
            print('fouls:', fouls)

            c.execute('''
                INSERT INTO player_stats_2122 (nba_player_id, first_name, last_name, nba_team_id, team_abbr,
                                            age, games_started, games_played, minutes, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct,
                                            ftm, fta, ft_pct, points, orebounds, drebounds, rebounds, assists, steals, blocks,
                                            turnovers, fouls)
                VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            ''',(nba_player_id, first_name, last_name, nba_team_id, team_abbr, age, games_started, games_played, minutes, fgm, fga,
                fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, points, orebounds, drebounds, rebounds, assists, steals, blocks,
                turnovers, fouls))
            conn.commit()
            print(name, 'successfully added to database')


    except Exception as e:
        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error_row = exc_traceback.tb_lineno
        print('name:', name)
        print('error:', str(e))
        with open('error_file.log', 'a') as error_file:
            error_file.write('Issue with at ' + now + '. Check code in row ' + str(error_row) + ' of check_for_new_players.py' + '\n')
            error_file.write('player: ' + name + '\n')
            error_file.write('error: ' + str(e))
            error_file.write(str(e) + '\n\n')        
        error_file.close()
import sqlite3
from nba_api.stats.endpoints import playercareerstats, playergamelog
from nba_api.stats.static import players
import time
from datetime import datetime
from sqlalchemy import except_all
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

# query database row by row
for i in range(number_of_rows):
    try:
        # query existing data in the database
        c.execute('''SELECT * FROM player_stats_2122 LIMIT 1 OFFSET (?);''',(str(i),))
        row = c.fetchall()[0]
        row = [x if (type(x) != float() or x.is_integer() == False) else int(x) for x in list(row)]
        # isolate player id to feed into PlayerCareerStatistics model

        nba_player_id = row[1]
        # isolate id to add to tuple
        id = row[0]
        # isolate name
        first_name = row[2]
        last_name = row[3]
        # isolate most recent stats
        most_recent_stats = playercareerstats.PlayerCareerStats(player_id=nba_player_id).get_data_frames()[0].iloc[-1]
        
        # remove unwanted columns and convert even floats to integers
        most_recent_stats.drop(['SEASON_ID','LEAGUE_ID'], inplace=True)
        # convert floats to integers as necessary  
        for j in range(len(most_recent_stats)):
            stat = most_recent_stats[j]
            if type(stat) != str:
                if type(stat) == float() and stat.is_integer() == True:
                    stat = int(stat)
                else:
                    stat = int(stat)

                most_recent_stats[j] = stat
        # create empty list to add player information into - used to compare against stats in the database
        up_to_date_stats = []
        up_to_date_stats.append(id)

        # nba player id
        nba_player_id = int(most_recent_stats['PLAYER_ID'])
        print('id:', nba_player_id)
        up_to_date_stats.append(nba_player_id)
        up_to_date_stats.append(first_name)
        up_to_date_stats.append(last_name)
        # nba team name 
        nba_team_id = int(most_recent_stats['TEAM_ID'])
        # how to handle if players have been on two teams in a season
        if nba_team_id == 0:
            nba_team_id = int(playercareerstats.PlayerCareerStats(player_id=nba_player_id).get_data_frames()[0].iloc[-2]['TEAM_ID'])
        else:
            nba_team_id = int(most_recent_stats['TEAM_ID'])
        print('nba_team_id:', nba_team_id)
        up_to_date_stats.append(nba_team_id)
        # nba team name
        team_abbr = most_recent_stats['TEAM_ABBREVIATION']
        if team_abbr == 'TOT':
            team_abbr = playercareerstats.PlayerCareerStats(player_id=nba_player_id).get_data_frames()[0].iloc[-2]['TEAM_ABBREVIATION']
        else:
            team_abbr = most_recent_stats['TEAM_ABBREVIATION']
        print('team_abbr:', team_abbr)
        up_to_date_stats.append(team_abbr)
        # age
        age = int(most_recent_stats['PLAYER_AGE'])
        print('age:', age)
        up_to_date_stats.append(age)
        # games played
        games_played = int(most_recent_stats['GP'])
        print('games_played:', games_played)
        up_to_date_stats.append(games_played)
        # games started
        games_started = int(most_recent_stats['GS'])
        print('games_started:', games_started)
        up_to_date_stats.append(games_started)
        # minutes
        minutes = int(most_recent_stats['MIN'])
        print('minutes:', minutes)
        up_to_date_stats.append(minutes)
        # field goals made
        fgm = int(most_recent_stats['FGM'])
        print('fgm:', fgm)
        up_to_date_stats.append(fgm)
        # field goals attempted
        fga = int(most_recent_stats['FGA'])
        print('fga:', fga)
        up_to_date_stats.append(fga)
        # field goal %
        try:
            fg_pct = "%0.3f" % round(float(fgm/fga),3)
        except:
            fg_pct = "%0.3f" % round(float(0), 3)
        print('fg_pct:', fg_pct)
        up_to_date_stats.append(fg_pct)
        # 3pt field goals made
        fg3m = int(most_recent_stats['FG3M'])
        print('fg3m:', fg3m)
        up_to_date_stats.append(fg3m)
        # 3pt field goals attempted
        fg3a = int(most_recent_stats['FG3A'])
        print('fg3a:', fg3a)
        up_to_date_stats.append(fg3a)
        # 3pt field goal %
        try:
            fg3_pct = "%0.3f" % round(float(fg3m/fg3a),3)
        except:
            fg3_pct = "%0.3f" % round(float(0), 3)
        print('fg3_pct:', fg3_pct)
        up_to_date_stats.append(fg3_pct)
        # free throws made
        ftm = int(most_recent_stats['FTM'])
        print('ftm:', fgm)
        up_to_date_stats.append(ftm)
        # free throws attempted
        fta = int(most_recent_stats['FTA'])
        print('fta:', fta)
        up_to_date_stats.append(fta)
        # free throw %
        try:
            ft_pct = "%0.3f" % round(float(ftm/fta),3)
        except:
            ft_pct = "%0.3f" % round(float(0), 3)
        print('ft_pct:', ft_pct)
        up_to_date_stats.append(ft_pct)
        # points
        points = int(most_recent_stats['PTS'])
        print('points:', points)
        up_to_date_stats.append(points)
        # rebounds
        orebounds = int(most_recent_stats['OREB'])
        print('orebounds:', orebounds)
        up_to_date_stats.append(orebounds)
        drebounds = int(most_recent_stats['DREB'])
        print('drebounds:', drebounds)
        up_to_date_stats.append(drebounds)
        rebounds = int(most_recent_stats['REB'])
        print('rebounds:', rebounds)
        up_to_date_stats.append(rebounds)
        # assists
        assists = int(most_recent_stats['AST'])
        print('assists:', assists)
        up_to_date_stats.append(assists)
        # steals
        steals = int(most_recent_stats['STL'])
        print('steals:', steals)
        up_to_date_stats.append(steals)
        # blocks
        blocks = int(most_recent_stats['BLK'])
        print('blocks:', blocks)
        up_to_date_stats.append(blocks)
        # turnovers
        turnovers = int(most_recent_stats['TOV'])
        print('turnovers:', turnovers)
        up_to_date_stats.append(turnovers)
        # fouls
        fouls = int(most_recent_stats['PF'])
        print('fouls:', fouls)
        up_to_date_stats.append(fouls)


        print('stats in database:')
        print(row)
        print('stats from nba.com:')
        print(up_to_date_stats)
        print('\n')  

        for j in range(len(row)):
            try:
                database_record = row[j]
                up_to_date_record = up_to_date_stats[j]
                column = columns[j]
                if database_record != up_to_date_record:
                    c.execute('''UPDATE player_stats_2122
                                SET {} = {}
                                WHERE player_id = {};
                                '''.format(column, up_to_date_record, id))
                    conn.commit()
                    print(first_name, last_name, column, 'updated from', database_record, 'to', up_to_date_record)
                    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                    with open('log.txt', 'a') as f:
                        f.write(column + ' for ' + first_name + ' ' + last_name + ' updated from ' + str(database_record) + ' to ' + str(up_to_date_record) + ' at ' + str(now) + '\n')
                    f.close()
            except Exception as e:
                now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                exc_type, exc_value, exc_traceback = sys.exc_info()
                row = exc_traceback.tb_lineno
                print('column:', column)
                print('db record:', database_record)
                print('up to date record:', up_to_date_record)
                with open('error_file.log', 'a') as error_file:
                    error_file.write('Issue with row ' + str(i) + ' at ' + now + '. Check code in row ' + str(row) + ' of update.py' + '\n')
                    error_file.write('column: ' + str(column) + ', db record: ' + str(database_record) + ', up to date record: ' + str(up_to_date_record) + '\n')
                    error_file.write(str(e) + '\n\n')        
                error_file.close()
        

        with open('log.txt', 'a') as f:
            f.write('\n')
        f.close()
        print('\n')
        time.sleep(0.6)



    except Exception as e:
        now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        row = exc_traceback.tb_lineno
        print(getattr(e, 'message', repr(e)))
        print(getattr(e, 'message', str(e)))
        print('row:', row)
        with open('error_file.log', 'a') as error_file:
            error_file.write('Issue with row ' + str(i) + ' at ' + now + '. Check code in row ' + str(row) + ' of update.py' + '\n')
            error_file.write(str(e) + '\n\n')        
        error_file.close()
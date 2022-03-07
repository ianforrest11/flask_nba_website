from nba_api.stats.endpoints import playercareerstats, playergamelog
from nba_api.stats.static import players
import time
import sqlite3

nba_players = players.get_players()
time.sleep(0.6)
# print(len(nba_players))

career = playercareerstats.PlayerCareerStats(player_id='203076')
# print(career.get_data_frames()[0])
print(career.get_data_frames()[0].columns)
time.sleep(0.6)

conn = sqlite3.connect('test_database.db') 
c = conn.cursor()

c.execute('''
    DROP TABLE IF EXISTS player_stats_2122;
''')

c.execute('''
          CREATE TABLE player_stats_2122
          ([player_id] INTEGER PRIMARY KEY,
           [nba_player_id] INTEGER,
           [first_name] VARCHAR,
           [last_name] VARCHAR,
           [nba_team_id] INTEGER,
           [team_abbr] VARCHAR,
           [age] INTEGER,
           [games_played] INTEGER,
           [games_started] INTEGER,
           [minutes] INTEGER,
           [fgm] INTEGER,
           [fga] INTEGER,
           [fg_pct] VARCHAR,
           [fg3m] INTEGER,
           [fg3a] INTEGER,
           [fg3_pct] VARCHAR,
           [ftm] INTEGER,
           [fta] INTEGER,
           [ft_pct] VARCHAR,
           [points] INTEGER,
           [orebounds] INTEGER,
           [drebounds] INTEGER,
           [rebounds] INTEGER,
           [assists] INTEGER,
           [steals] INTEGER,
           [blocks] INTEGER,
           [turnovers] INTEGER,
           [fouls] INTEGER
           );
          ''')                
conn.commit()

c.execute(
'''PRAGMA table_info(player_stats_2122)''')
rows = c.fetchall()
print('columns:', rows)

# game_log = playergamelog.PlayerGameLog(player_id='203076')
# print(game_log.get_data_frames()[0].head())

for player in nba_players:
    name = player['full_name']
    first_name = player['first_name']
    last_name = player['last_name']
    id = player['id']

    player_career_stats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()[0]
    try:
        most_recent_season = player_career_stats.iloc[-1]
    except:
        print(name, ' error')
        print(player_career_stats)
        print('\n')
    if most_recent_season['SEASON_ID'] == '2021-22':
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
        # if i == 0:
        c.execute('''SELECT * FROM player_stats_2122 AS ps WHERE ps.first_name || " " || ps.last_name = (?) || " " || (?);''', (first_name, last_name,))
        row = c.fetchall()[0]
        print(row)
        print('\n')
    time.sleep(0.6)

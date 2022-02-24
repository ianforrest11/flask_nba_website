from nba_api.stats.endpoints import playercareerstats, playergamelog
from nba_api.stats.static import players
import time

nba_players = players.get_players()
time.sleep(0.6)
# print(len(nba_players))

# career = playercareerstats.PlayerCareerStats(player_id='203076')
# print(career.get_data_frames()[0])
# print(career.get_data_frames()[0].columns)
# time(0.6)

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
    if most_recent_season['SEASON_ID'] == '2021-22':
        print('name:', name)
        print('id:', id)
        print(name, 'is a current player')
        ppg = round(int(most_recent_season['PTS'])/int(most_recent_season['GP']), 1)
        print('PPG:', ppg)
        rpg = round(int(most_recent_season['REB'])/int(most_recent_season['GP']), 1)
        print('RPG:', rpg)
        apg = round(int(most_recent_season['AST'])/int(most_recent_season['GP']), 1)
        print('APG:', apg)
        spg = round(int(most_recent_season['STL'])/int(most_recent_season['GP']), 1)
        print('SPG:', spg)
        bpg = round(int(most_recent_season['BLK'])/int(most_recent_season['GP']), 1)
        print('BPG:', bpg)
        print('\n')
    time.sleep(0.6)

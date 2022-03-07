import pandas as pd
import sqlite3
from datetime import datetime

# connect to database
conn = sqlite3.connect('test_database.db') 
c = conn.cursor()

c.execute('''PRAGMA table_info(player_stats_2122);''')
columns = [x[1] for x in c.fetchall()]
print(columns)

print(float("%0.3f" % 10))

c.execute('''SELECT * FROM player_stats_2122 AS ps WHERE ps.first_name || " " || ps.last_name = (?) || " " || (?);''', ('Armoni', 'Brooks',))
row = c.fetchall()[0]
print(row)



# for i in range(1):
#     most_recent_stats = pd.Series([1629638, 0, 'TOT', 23.0, 52, 19, 1322.0, 237, 633, 0.374, 95, 306, 0.31, 70, 97, 0.722, 36, 129, 165, 139, 41, 19, 85, 88, 639])

#     most_recent_stats = [x if (type(x) != float or x.is_integer() == False) else int(x) for x in list(most_recent_stats)]
#     print(most_recent_stats)


    
# conn = sqlite3.connect('test_database.db')
# c = conn.cursor()

# columns = c.execute("PRAGMA table_info(player_stats_2122)")
# columns_query = [item[1] for item in columns.fetchall()]
# print(columns_query)

# c.execute("DROP TABLE IF EXISTS display_stats")
# c.execute('''
#     CREATE TABLE display_stats
#     AS
#     SELECT first_name AS "First Name", last_name AS "Last Name", team_abbr,
#     age, games_played, games_started, minutes, fgm, fga,
#     fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, points AS "PTS",
#     orebounds, drebounds, rebounds AS "REB", assists, steals, blocks, 
#     turnovers, fouls 
#     FROM player_stats_2122;''')


# set_columns_query = c.execute('''PRAGMA table_info(display_stats)''').fetchall()
# print(set_columns_query)

# conn.close()
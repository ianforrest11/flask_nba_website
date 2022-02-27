import pandas as pd

for i in range(1):
    most_recent_stats = pd.Series([1629638, 0, 'TOT', 23.0, 52, 19, 1322.0, 237, 633, 0.374, 95, 306, 0.31, 70, 97, 0.722, 36, 129, 165, 139, 41, 19, 85, 88, 639])

    most_recent_stats = [x if (type(x) != float or x.is_integer() == False) else int(x) for x in list(most_recent_stats)]
    print(most_recent_stats)
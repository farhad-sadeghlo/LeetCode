
#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id', 'event_date'])
    activity['games_played_so_far'] = activity.groupby('player_id')['games_played'].cumsum()
    return activity[['player_id','event_date','games_played_so_far']]
#IMPORTANT!! Submit Code Region End(Do not remove this line)
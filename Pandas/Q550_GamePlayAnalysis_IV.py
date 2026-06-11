
#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id','event_date'])
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    first_login_date = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login_date['next_day'] = first_login_date['event_date'] + pd.DateOffset(days=1)
    next_day_login = first_login_date.merge(activity, left_on=['player_id', 'next_day'], right_on=['player_id', 'event_date'], how='inner')
    count = next_day_login['player_id'].nunique()
    total_players = activity['player_id'].nunique()
    fraction = round(count / total_players, 2) if total_players else 0
    return pd.DataFrame({'fraction': [fraction]})

#IMPORTANT!! Submit Code Region End(Do not remove this line)


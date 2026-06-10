
#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather['prevDate'] = weather['recordDate'] - pd.DateOffset(days=1)
    merged = weather.merge(weather, left_on='prevDate', right_on='recordDate', suffixes=('_x', '_y'))

    return merged.loc[merged['temperature_x'] > merged['temperature_y'], ['id_x']].rename(columns={'id_x':'Id'})
#IMPORTANT!! Submit Code Region End(Do not remove this line)
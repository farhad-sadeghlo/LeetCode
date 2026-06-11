
#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # counts = orders.groupby('customer_number').size()
    # customer = counts.idxmax()
    # return pd.DataFrame({'customer_number': [customer]})

    counts = orders['customer_number'].value_counts().idxmax()
    return pd.DataFrame({'customer_number': [counts]})
#IMPORTANT!! Submit Code Region End(Do not remove this line)
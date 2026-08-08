
#leetcode submit region begin(Prohibit modification and deletion)
import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:

    if len(friend_request) == 0:
        accepted_rate = 0.0
    else:
        accepted = request_accepted[['requester_id', 'accepter_id']].drop_duplicates()
        requests = friend_request[['sender_id', 'send_to_id']].drop_duplicates()

        accepted_rate = round(len(accepted)/len(requests), 2)

    return pd.DataFrame({'accept_rate': [accepted_rate]})
#leetcode submit region end(Prohibit modification and deletion)


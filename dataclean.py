import pandas as pd
from time import time
from tensor import Tensor

def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def transform_csv_to_liner_tensor(df):
    df.fillna(0)
    user_id_list = list(deque(df.index.values))
    users_tensor = dict()
    # help debug
    user_time = 0
    user_count = len(user_id_list)
    print "total user_count:", user_count 
    for user_id in user_id_list:
        print "the times:", user_time,
        print "the user_id:", user_id,
        user_tensor_info = df.ix[user_id, ['merchant_id', 'activity_log']]
        specific_user_tensor = Tensor(user_tensor_info) 
        specific_user_tensor.build_tensor()
        users_tensor[user_id] = specific_user_tensor
        user_time = user_time + 1
        print "percent:", user_time/user_count    
     
    return users_tensor

def get_clean_csv(df, users_tensor):
    first_time = True
    for user_id, user_tensor in users_tensor.items():
        if user_tensor.is_crawler():
            continue
        user_delete_index_list = user_tensor.is_one_click()    
        user_df = df.ix[user_id]
        user_df = user_df.reset_index()
        user_df = user_df.drop(user_delete_index_list)
        if first_time:
            user_df.to_csv('clean_data.csv', header=True, index=False)
            first_time = False
        else:
            user_df.to_csv('clean_data.csv', header=False, index=False,\
             mode='wa+')        


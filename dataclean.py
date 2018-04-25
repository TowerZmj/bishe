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

def delete_user(df, user_id):
    pass

def delete_user_with_index(df, user_id, user_delete_index_list):
    pass

def clean_dirty_data(df, users_tensor):
    for user_id, user_tensor in users_tensor.items():
        if user_tensor.is_crawler():
            delete_user(df, user_id)
            continue
        user_delete_index_list = user_tensor.is_one_click()    
        delete_user_with_index(df, user_id, user_delete_index_list)

def main():
    df = pd.read_csv('train_format2.csv', index_col='user_id')
    users_tensor = transform_csv_to_liner_tensor(df)
    clean_dirty_data(df, users_tensor)
    
if __name__ == '__main__':
    print 'start'
    start = time()
    main()
    end = time()
    print 'end'
    diff_time = end - start
    print 'diff time', diff_time

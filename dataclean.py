import pandas as pd
from time import time
from tensor import Tensor

def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def transform_csv_to_liner_tensor(csv_file_name):
    df = pd.read_csv(csv_file_name, index_col='user_id')
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


def main():
    users_tensor = transform_csv_to_liner_tensor('train_format2.csv')

if __name__ == '__main__':
    print 'start'
    start = time()
    main()
    end = time()
    print 'end'
    diff_time = end - start
    print 'diff time', diff_time

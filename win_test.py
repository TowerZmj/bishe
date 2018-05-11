import pandas as pd
from time import time
from dataclean.dataclean import *
from dataclean.analysis import *


def main():
    df = pd.read_csv('win_test.csv', index_col='user_id')
    users_tensor = transform_csv_to_liner_tensor(df)
    user_id_list = list(deque(df.index.values))
    # draw_test()
    # draw_users_brows_columnar(user_id_list, users_tensor, 5)
    draw_users_dirty_columnar(user_id_list, users_tensor)
    # get_clean_csv(df, users_tensor)


if __name__ == '__main__':
    print 'start'
    start = time()
    main()
    end = time()
    print 'end'
    diff_time = end - start
    print 'diff time', diff_time


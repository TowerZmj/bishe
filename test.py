import pandas as pd
from tensor import Tensor


def main():
    df = pd.read_csv('train_format2.csv', index_col='user_id')

    specific_user_tensor_info = df.ix[34176, ['merchant_id', 'activity_log']]
    
    specific_user_tensor = Tensor(specific_user_tensor_info)

    specific_user_tensor.build_tensor()

    one_click_list = specific_user_tensor.is_one_click()
    
    user_df = df.ix[34176]
    user_df = user_df.reset_index()
    user_df = user_df.drop(one_click_list) 
    user_df.to_csv('34176_clean_data.csv', index=False)    


if __name__ == '__main__':
    main()

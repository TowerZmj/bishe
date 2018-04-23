import pandas as pd
import numpy as np
import math

class Tensor:
    def __init__(self, tensor_info):
        self.merchant_id = tensor_info['merchant_id']
        self.activity_log = tensor_info['activity_log']
        
    def build_tensor(self):
        x_length = self.merchant_id.size
        y_length = 4
        self.tensor = np.zeros((x_length, y_length))
        
        if x_length == 1:
            self.merchant_id = pd.Series(self.merchant_id)
            
        merchant_id_arr = self.merchant_id.values
        activity_log_arr = self.activity_log.values
        for i in range(x_length):
            specific_merchant_activity_log = activity_log_arr[i]
            
            # print specific_merchant_activity_log
            # the data is nan 
            if type(specific_merchant_activity_log) != str:
                print specific_merchant_activity_log, 'nan data'
                for j in range(y_length):
                    self.tensor[i][j] = -1
                continue
                
            # print specific_merchant_activity_log
            specific_merchant_type_log = self.analysis_activity_log(\
                specific_merchant_activity_log)
            specific_merchant_type_log_series = pd.Series(\
                specific_merchant_type_log)
            type_value_counts = specific_merchant_type_log_series.\
                value_counts()
            type_index = type_value_counts.index
            for j in range(y_length):
                if j in type_index:
                    self.tensor[i][j] = type_value_counts[j]
      
    def analysis_activity_log(self, activity_log):
        activity_type_log = list()
        activity_log_list = activity_log.split('#')
        for log in activity_log_list:
            log_field = log.split(':')
            activity_type_log.append(int(log_field[4]))
        
        return activity_type_log
    
    def is_crawler(self):
        pass

    def is_one_click(self):
        pass


from dataclean import *

def main():
    df = pd.read_csv('test1.csv', index_col='user_id')
    users_tensor = transform_csv_to_liner_tensor(df)
    get_clean_csv(df, users_tensor)     
 
if __name__ == '__main__':
    print 'start'
    start = time()
    main()
    end = time()
    print 'end'
    diff_time = end - start
    print 'diff time', diff_time

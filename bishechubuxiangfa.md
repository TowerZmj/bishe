 # pandas 读取数据

* pd.read_csv()
* 将user_id作为下标索引
* 可以得到总共的user_id，然后通过user_id得到merchant_id的集合，对于每一个user_id都对应的有一个merchant_id的集合，然后通过merchant_id以及四种行为，形成一个对应的张量
* 形成的二阶张量
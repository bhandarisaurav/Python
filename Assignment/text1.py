import pandas as pd

dic = {'key1':['v1','v2'], 'key2':['vv','gg']}

pd.DataFrame(dic).T.reset_index().to_csv('myfile.csv', header=False, index=False)
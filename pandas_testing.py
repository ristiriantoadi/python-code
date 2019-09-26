import pandas as pd

# df = pd.DataFrame([[1, 2, 3, 4, 5], [3, 3, 3, 4, 5]], columns=[
#                   'a', 'b', 'c', 'd', 'e'])
# print(df)
abc = pd.read_csv('zoo.csv')
print(abc['uniq_id'])

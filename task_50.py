import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

encoded_data = data.copy()

unique_values = data['whoAmI'].unique()

for value in unique_values:
    encoded_data[value] = (data['whoAmI'] == value).astype(int)

encoded_data.drop('whoAmI', axis=1, inplace=True)

print(encoded_data.head())
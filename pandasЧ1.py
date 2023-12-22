import pandas as pd
import numpy as np
dict = {
    'Count': [1, 2, 3, 4, 5],
    '+': [2, 4, 6, 8, 10],
    '**':[1, 4, 9, 16, 25]
}
df = pd.DataFrame(dict, index=[i for i in range(6880, 6885)])
print(df)
#nomer 2
print(df.tail(3))
print(df.head(3))
#nomer 3
df.to_csv('My first project')
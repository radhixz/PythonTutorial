import numpy as np
import pandas as pd
import json

files = ['file1', 'file2', 'file3']
json_files = json.dumps(files)
print(json_files)

params = ','.join(['?'] * len(files))
print(params)
x = pd.DataFrame(np.random.randn(6,4), index=[4,3,5, 2, 1, 6] ,columns=['A', 'B', 'C', 'D'])

print(x)
y = x.sort_values(by='A')
print(y)
# https://towardsdatascience.com/modin-accelerating-your-pandas-functions-by-changing-one-line-of-code-504c39b5ddbc

#%%

### Read in the data with Pandas
import pandas as pd
import time 

s = time.time()
df = pd.read_csv("data/esea_master_dmg_demos.part1.csv")
e = time.time()
print("Pandas Loading Time = {}".format(e-s))

### Read in the data with Modin
import modin.pandas as pd

s = time.time()
df = pd.read_csv("data/esea_master_dmg_demos.part1.csv")
e = time.time()
print("Modin Loading Time = {}".format(e-s))

# %%
import pandas as pd
df = pd.read_csv("data/esea_master_dmg_demos.part1.csv")

s = time.time()
df = pd.concat([df for _ in range(5)])
e = time.time()
print("Pandas Concat Time = {}".format(e-s))

import modin.pandas as pd
df = pd.read_csv("data/esea_master_dmg_demos.part1.csv")

s = time.time()
df = pd.concat([df for _ in range(5)])
e = time.time()
print("Modin Concat Time = {}".format(e-s))

# %%

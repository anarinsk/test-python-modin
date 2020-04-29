### https://medium.com/sfu-cspmp/up-the-data-processing-ante-with-pandas-modin-ray-b354bb9401

#%% 
import pandas as pandas_pd
%time  pandas_df = pandas_pd.read_csv("data/kiva_loans.csv")

#%%
import os
os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask
from distributed import Client
client = Client(memory_limit='8GB', processes=False)
import modin.pandas as dask_pd
%time  mdask_df = dask_pd.read_csv("data/kiva_loans.csv")

# %%
import os
os.environ["MODIN_ENGINE"] = "ray"  # Modin will use Ray
import ray
#ray.init(memory=5242880000)
import modin.pandas as ray_pd
%time  mray_df = ray_pd.read_csv("data/kiva_loans.csv")

# %%
%time df1 = pandas_df.append(pandas_df)
%time df2 = mdask_df.append(mdask_df)
%time df3 = mray_df.append(mray_df)

# %%
%time df1 = pandas_pd.concat([pandas_df for _ in range(5)])
%time df2 = dask_pd.concat([mdask_df for _ in range(5)])
%time df3 = ray_pd.concat([mray_df for _ in range(5)])

# %%
%time pandas_pd.isnull(pandas_df["use"])
%time dask_pd.isnull(mdask_df["use"])
%time ray_pd.isnull(mray_df["use"])

# %%
%time pandas_df.fillna(value=0)
%time mdask_df.fillna(value=0)
%time mray_df.fillna(value=0)

# %%

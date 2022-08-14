#%%
import xdrlib
import pandas as pd
import numpy as np


# %%
df = pd.read_csv ("armenian_pubs - armenian_pubs.csv")

# %%
df.shape

# %%
df
# %%
df.info()

#%%
df_Fav_Pub = df[(df["Fav_Pub"]== "Fav_Pub")]
#%%
df

# %%
#most favourite pub in Armenia 
pd.pivot_table(df,index=["Freq"],values=["Fav_Pub",],aggfunc=[np.mean,len,sum])

# %%
#the most favourite pub among female and male visitors
pd.pivot_table(df,index=["Gender"],values=["Fav_Pub", "Freq"],aggfunc=[np.mean,len,sum])
#%%
#the most favourite pub among female and male visitors
dfnew=pd.pivot_table(df,index=["Gender"],values=["Fav_Pub", "Freq"],aggfunc=[np.mean,len,sum])
dfnew.to_csv('C:\\export.csv')
df

#%%
df.to_csv('C:\\export.csv')
df
#%%
df_new = pd.pivot_table(df, index=["Freq"],values=["Fav_Pub",],aggfunc=[np.mean,len,sum])
#%%


# %%
df_Fav_Pub = df[(df["Fav_Pub"]== "Fav_Pub")] 

# %%
#19 is the age that was given most of the times
pd.pivot_table(df,index=["Age"], values=["Freq"],aggfunc=[np.mean,len,sum])

# %%
#What are most people willing to spend at the pub?
pd.pivot_table(df,index=["Fav_Pub"], values=["WTS", "Freq"],aggfunc=[np.mean,len,sum])
#%%
df.to_csv (#the most favourite pub among female and male visitors
pd.pivot_table(df,index=["Gender"],values=["Fav_Pub", "Freq"],aggfunc=[np.mean,len,sum]))
# %%
df
# %%
#save the data to csv file
df.to_csv("armenian_pubs - armenian_pubs.csv")
# %%
df
# %%
df.to_csv('C:\\export.csv')


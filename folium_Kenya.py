#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import folium

data = {'store':['nairobifoods','kajiadofoods','nakurufoods','kisumufoods'],
        'latitude':[-1.302473, -1.3999999, -0.303099,-0.091702],
        'longitude':[36.7451004,36.6293008,36.080025,34.767956],
        'revenue':[600000,120000,30000,40000]
        }


# In[2]:


df = pd.DataFrame(data)
df


# In[3]:


center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location = center, zoom_start=6 , min_zoom=5, max_zoom=8)
map_kenya


# In[4]:


for index, franchise in df.iterrows():
    location = [franchise['latitude'], franchise['longitude']]
    folium.Marker(location, popup=f"Name: {franchise['store']}\n Revenue($): {franchise['revenue']}").add_to(map_kenya)
map_kenya


# In[ ]:





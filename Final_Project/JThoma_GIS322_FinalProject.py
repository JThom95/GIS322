
### Import all necessary modules
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


### Load in CSV with state names, covid deaths, covid cases, and gini index
data = pd.read_csv('COVID19_state.csv')

### Use pandas to read csv data into a DataFrame 
COVID_df = pd.DataFrame(data, columns=['State','Infected','Deaths','Gini'])

### Add a new column to dataFrame and calculate COVID death rate (%)
COVID_df['DeathRate'] = (COVID_df.Deaths / COVID_df.Infected)*100

### Read in state boundaries shapefile as a geoDataFrame
states = gpd.read_file('cb_2018_us_state_20m.shp')
states = states.rename(columns={'NAME':'State'})

### Merge dataFrame with COVID information into the states GeoDataFrame by state name 
states_allData = states.merge(COVID_df, on = 'State')


### Create a color map showing the percentage of COVID deaths per state
lower48 = states_allData[(states_allData.State != "Alaska") & 
(states_allData.State != 'Hawaii') & (states_allData.State != 'Puerto Rico')] 
fig, ax = plt.subplots(1, figsize=(16, 12))
lower48.plot(column="DeathRate",figsize=(16,12), ax=ax, cmap='YlOrRd',edgecolor='black', linewidth=0.2)

vmin = lower48["DeathRate"].min()
vmax = lower48["DeathRate"].max()

plt.title("USA: COVID-19 Death Rate",fontdict={'fontsize':20, 'fontweight':'bold'})
    
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax),cmap='YlOrRd')
divider = make_axes_locatable(ax)
cax = divider.append_axes("left", size="2%", pad = 0.05)
fig.colorbar(sm,label='Percent',cax=cax,)

plt.savefig("Figure1",dpi=400,bbox_inches='tight')


### Create a color map showing the Gini Index per state
lower48 = states_allData[(states_allData.State != "Alaska") & 
(states_allData.State != 'Hawaii') & (states_allData.State != 'Puerto Rico')] 
fig, ax = plt.subplots(1, figsize=(16, 12))
lower48.plot(column="Gini",figsize=(16,12), ax=ax, cmap='YlOrRd',edgecolor='black', linewidth=0.2)

vmin = lower48["Gini"].min()
vmax = lower48["Gini"].max()

plt.title("USA: Gini Index",fontdict={'fontsize':20, 'fontweight':'bold'})
    
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax),cmap='YlOrRd')
divider = make_axes_locatable(ax)
cax = divider.append_axes("left", size="2%", pad = 0.05)
fig.colorbar(sm,cax=cax,)

plt.savefig("Figure2",dpi=400,bbox_inches='tight')


# Create a scatterplot comparing the death rate and the Gini index 
fig = plt.figure(3, figsize=(12,8))

x = lower48.Gini
y = lower48.DeathRate

plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),'-r')

plt.xlabel('Gini Index', fontdict={'fontsize':12, 'fontweight':'bold'})
plt.ylabel('Covid Death Rate (%)', fontdict={'fontsize':12, 'fontweight':'bold'})

plt.title("USA: Gini Index vs COVID Death Rate",fontdict={'fontsize':20, 'fontweight':'bold'})

plt.savefig("Figure3",dpi=400,bbox_inches='tight')

# Global Terrorism Analysis 

This jupyter file consists of TWO parts: 
<li> Part ONE: Data Preparation and Introduction 
<li> Part TWO: Findings and Analysis


```python
import pandas as pd
import numpy as np
import seaborn as sns
%pylab inline

import sklearn as sk
import sklearn.tree as tree
from IPython.display import Image  
import pydotplus
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn3, venn3_circles
import matplotlib.image as mpimg
%autosave 0
```

    Populating the interactive namespace from numpy and matplotlib




    Autosave disabled


#  PART ONE : Data Preparation and Introduction

# Data Preparation

## 1.1  Description Of Raw Dataset


```python
df_raw = pd.read_csv('globalterrorismdb_0617dist.csv')
```


```python
df_raw.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>eventid</th>
      <th>iyear</th>
      <th>imonth</th>
      <th>iday</th>
      <th>approxdate</th>
      <th>extended</th>
      <th>resolution</th>
      <th>country</th>
      <th>country_txt</th>
      <th>region</th>
      <th>...</th>
      <th>addnotes</th>
      <th>scite1</th>
      <th>scite2</th>
      <th>scite3</th>
      <th>dbsource</th>
      <th>INT_LOG</th>
      <th>INT_IDEO</th>
      <th>INT_MISC</th>
      <th>INT_ANY</th>
      <th>related</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>197000000001</td>
      <td>1970</td>
      <td>7</td>
      <td>2</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>58</td>
      <td>Dominican Republic</td>
      <td>2</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PGIS</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>197000000002</td>
      <td>1970</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>130</td>
      <td>Mexico</td>
      <td>1</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PGIS</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>197001000001</td>
      <td>1970</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>160</td>
      <td>Philippines</td>
      <td>5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PGIS</td>
      <td>-9</td>
      <td>-9</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 135 columns</p>
</div>




```python
shape(df_raw)
```




    (170350, 135)




```python
print("This Dataset records "+ str(len(df_raw)) +" terrorist attacks"+"\n"+"And"+ " contains "+ str(len(df_raw.columns))+ " variables")
```

    This Dataset records 170350 terrorist attacks
    And contains 135 variables


<li>To pick up some meaningful variables in 135 variables, we use both functional method and manual one.  The following count_null function can get the null_value percentage of each varibale. As we can see from the results, there are 64 variables whose null_value percentage higher than 90%.  
<li>Also,we double checked with remained varibales and excluded several invaluable varibales. 


```python
df_raw.columns
```




    Index([u'eventid', u'iyear', u'imonth', u'iday', u'approxdate', u'extended',
           u'resolution', u'country', u'country_txt', u'region',
           ...
           u'addnotes', u'scite1', u'scite2', u'scite3', u'dbsource', u'INT_LOG',
           u'INT_IDEO', u'INT_MISC', u'INT_ANY', u'related'],
          dtype='object', length=135)




```python
def countnull(countdf):
    colname_list=[]
    True_list=[]
    False_list=[]
    for idx,i in zip(countdf.columns, range(0,len(countdf.columns))):
        if countdf.iloc[:,i].isnull().value_counts()[0] != len(countdf):
            colname_list.append(idx)
            True_list.append(countdf.iloc[:,i].isnull().value_counts()[1])
            False_list.append(countdf.iloc[:,i].isnull().value_counts()[0])
    count_null=pd.DataFrame({'colname_list': colname_list,'Null': True_list,'Not_Null': False_list})
    count_null['Null_Percentage']= count_null.Null*1.0/(count_null.Not_Null+count_null.Null)
    Count_table= count_null.sort_values(by='Null_Percentage', ascending=False)
    Count_table=Count_table[Count_table.Null_Percentage>0.9]
    return Count_table
```


```python
countnull(df_raw).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Not_Null</th>
      <th>Null</th>
      <th>colname_list</th>
      <th>Null_Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>41</th>
      <td>13</td>
      <td>170337</td>
      <td>gsubname3</td>
      <td>0.999924</td>
    </tr>
    <tr>
      <th>70</th>
      <td>71</td>
      <td>170279</td>
      <td>weapsubtype4</td>
      <td>0.999583</td>
    </tr>
    <tr>
      <th>71</th>
      <td>71</td>
      <td>170279</td>
      <td>weapsubtype4_txt</td>
      <td>0.999583</td>
    </tr>
    <tr>
      <th>69</th>
      <td>74</td>
      <td>170276</td>
      <td>weaptype4_txt</td>
      <td>0.999566</td>
    </tr>
    <tr>
      <th>68</th>
      <td>74</td>
      <td>170276</td>
      <td>weaptype4</td>
      <td>0.999566</td>
    </tr>
  </tbody>
</table>
</div>



## 1.2 Data Cleaning

#### Notes:
<li>1.  Choose:  the varibales we need to use  and rename those varibales 
<li>2.  Create Total_num:  measures the total number of person got killed and wounded in each terrirsm attack.
<li>3.  Create dummy 'Casualities' :  some one got killed or wounded in a terrism attack, set the value into 1, otherwise 0.
<li>4.  For more data cleaning contents, we put them in seperate finding parts.


```python
df_raw.rename(columns={'iyear':'Year',
                   'imonth':'Month',
                   'iday':'Day',
                   'country_txt':'Country',
                   'region_txt':'Region',
                   'attacktype1_txt':'AttackType',
                   'target1':'Target',
                   'nkill':'Killed',
                   'nwound':'Wounded',
                   'summary':'Summary',
                   'gname':'Group',
                   'targtype1_txt':'Target_type',
                   'targsubtype1_txt':'Sub_Target_type',
                   'weapsubtype1_txt':'Sub_Weapon_type',
                   'weaptype1_txt':'Weapon_type',
                   'suicide':'suicide',
                   'motive':'Motive'},inplace=True)
df=df_raw[['Year','Month','Day','Country','Region','city','latitude','longitude'
       ,'AttackType','Killed','Wounded','Target','Group','Target_type','Sub_Target_type',\
          'success', 'suicide','Weapon_type','Sub_Weapon_type','Motive','Summary','addnotes']]
df['Total_num']=df.Wounded+df.Killed
df.loc[:,'casualities']  = np.where((df.Killed + df.Wounded)>0.0, 1, 0)
```

    /anaconda3/envs/py27/lib/python2.7/site-packages/ipykernel_launcher.py:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy



```python
df=df[(df.Month!= 0)&(df.Day!= 0)]
df=df.drop(['Target'],axis=1) 
```


```python
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Country</th>
      <th>Region</th>
      <th>city</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>AttackType</th>
      <th>Killed</th>
      <th>...</th>
      <th>Sub_Target_type</th>
      <th>success</th>
      <th>suicide</th>
      <th>Weapon_type</th>
      <th>Sub_Weapon_type</th>
      <th>Motive</th>
      <th>Summary</th>
      <th>addnotes</th>
      <th>Total_num</th>
      <th>casualities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1970</td>
      <td>7</td>
      <td>2</td>
      <td>Dominican Republic</td>
      <td>Central America &amp; Caribbean</td>
      <td>Santo Domingo</td>
      <td>18.456792</td>
      <td>-69.951164</td>
      <td>Assassination</td>
      <td>1.0</td>
      <td>...</td>
      <td>Named Civilian</td>
      <td>1</td>
      <td>0</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1970</td>
      <td>1</td>
      <td>1</td>
      <td>United States</td>
      <td>North America</td>
      <td>Cairo</td>
      <td>37.005105</td>
      <td>-89.176269</td>
      <td>Armed Assault</td>
      <td>0.0</td>
      <td>...</td>
      <td>Police Building (headquarters, station, school)</td>
      <td>1</td>
      <td>0</td>
      <td>Firearms</td>
      <td>Unknown Gun Type</td>
      <td>To protest the Cairo Illinois Police Deparment</td>
      <td>1/1/1970: Unknown African American assailants ...</td>
      <td>The Cairo Chief of Police, William Petersen, r...</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1970</td>
      <td>1</td>
      <td>2</td>
      <td>Uruguay</td>
      <td>South America</td>
      <td>Montevideo</td>
      <td>-34.891151</td>
      <td>-56.187214</td>
      <td>Assassination</td>
      <td>0.0</td>
      <td>...</td>
      <td>Police Security Forces/Officers</td>
      <td>0</td>
      <td>0</td>
      <td>Firearms</td>
      <td>Automatic Weapon</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 23 columns</p>
</div>




```python
shape(df)
```




    (169459, 23)




```python
df.columns.unique()
```




    Index([u'Year', u'Month', u'Day', u'Country', u'Region', u'city', u'latitude',
           u'longitude', u'AttackType', u'Killed', u'Wounded', u'Group',
           u'Target_type', u'Sub_Target_type', u'success', u'suicide',
           u'Weapon_type', u'Sub_Weapon_type', u'Motive', u'Summary', u'addnotes',
           u'Total_num', u'casualities'],
          dtype='object')



## 1.3 Important Columns:

<li><b>Year：</b> This field contains the year in which the incident occurred. 

<li><b>Month：</b>This field contains the number of the month in which the incident occurred.

<li><b>Day：</b>This field contains the numeric day of the month on which the incident occurred.
 

<li><b>Country： </b>This field identifies the country or location where the incident occurred.Separatist regions, such as Kashmir, Chechnya, South Ossetia, Transnistria, or Republic of Cabinda, are coded as part of the “home” country. In the case where the country in which an incident occurred cannot be identified, it is coded as “Unknown.”

<li><b>Region：</b>This field identifies the region in which the incident occurred. The regions are divided into 12 categories.

<li><b>City： </b>This field contains the name of the city, village, or town in which the incident occurred. If the city, village, or town for an incident is unknown, then this field contains the smallest administrative area below provstate which can be found for the incident (e.g., district).

<li><b>Latitude: </b>This field records the latitude (based on WGS1984 standards) of the city in which the event occurred.

<li><b>Longitude: </b>This field records the longitude (based on WGS1984 standards) of the city in which the event occurred.

<li><b>Attack Type: </b>This field captures the general method of attack and often reflects the broad class of tactics used. It consists of nine categories：Assassination, Hijacking, Kidnapping, Barricade Incident, Bombing/Explosion, Armed Assault, Unarmed Assault, Facility/Infrastructure Attack, Unknown

<li><b>Killed： </b>This field stores the number of total confirmed fatalities for the incident. The number includes all victims and attackers who died as a direct result of the incident. 

<li><b>Wounded： </b>This field records the number of confirmed non-fatal injuries to both perpetrators and victims. It follows the conventions of the “Total Number of Fatalities” field described above.

<li><b>Group: </b> This field contains the name of the group that carried out the attack. In order to ensure consistency in the usage of group names for the database, the GTD database uses a standardized list of group names that have been established by project staff to serve as a reference for all subsequent entries.

<li><b>Target_type: </b> The target/victim type field captures the general type of target/victim. When a victim is attacked specifically because of his or her relationship to a particular person, such as a prominent figure, the target type reflects that motive. This variable consists of the 22 categories.

<li><b>Sub_Target: </b>The target subtype variable captures the more specific target category and provides the next level of designation for each target type. If a target subtype is not applicable this variable is left blank. 

<li><b>Weapon_type: </b>This field records the general type of weapon used in the incident. 

<li><b>Sub_Weapon_type: </b>This field records a more specific value for most of the Weapon Types identified immediately above. 

<li><b>Motive:</b> When reports explicitly mention a specific motive for the attack, this motive is recorded in the “Motive” field. This field may also include general information about the political, social, or economic climate at the time of the attack if considered relevant to the motivation underlying the incident.

<li><b>Summary: </b>A brief narrative summary of the incident, noting the “when, where, who, what, how,and why".

<li><b>addnotes:</b>This field is used to capture additional relevant details about the attack.

<li><b>Success：</b>Success of a terrorist strike is defined according to the tangible effects of the attack. Success is not judged in terms of the larger goals of the perpetrators. 1 = "Yes" The incident was successful. 0 = "No" The incident was not successful

<li><b>Suicide Attack： </b>This variable is coded “Yes” in those cases where there is evidence that the perpetrator did not intend to escape from the attack alive.

<li><b>Total_num：</b> This field measures the total number of person got killed and wounded in each terrirsm attack.

<li><b>Casualities:</b> some one got killed or wounded in a terrism attack, set the value into 1, otherwise 0.

# Introduction

Research Question: 
How have economic conditions improved, but exposures instead increased globally ?

## 1.1  Terrorism By Year On Different Regions 


```python
df_region=pd.crosstab(df.Year,df.Region)
df_region.plot(color=sns.color_palette('Set2',12))
fig=plt.gcf()
fig.set_size_inches(18,6)
plt.show()
```


![png](output_26_0.png)


## 1.2 Terrorism By Motives


```python
back_pic = mpimg.imread('movtive_mask.png') 
back_pic.shape
plt.imshow(back_pic) 
plt.axis('off') 
fig=plt.gcf()
fig.set_size_inches(18,10) 
plt.show()
```


![png](output_28_0.png)


# PART TWO : Findings and Analysis

From the dataset, we found the following three findings:
    1. Deadliest And Most Active Terrorist Groups You Didn’t Know ! 
    2. Why Terrorism in Western Europe Brought Low Causualties?
    3. Are Oil or Gas Primary Targets for Terrorists? NO!

# Finding 1:  Deadliest And Most Active Terrorist Groups You Didn’t Know ! 

Regarding all groups. How deadliest they are?  How active they are? Any similarities? Any differences?  

# 1.1  Assumption

<li> Deadliest group and Active groups must share a lot of difference in weapons and attack types so that different terrisim attack led to two different results: (attack most)  or  (causalities most)

## 1.1.1 Terrorist Groups By Attack Times & Num_Casualties: 
The dataset records the terrorist incidents by more than 3000 terrism groups.


```python
len(df.Group.unique())
```




    3434



The code below shows if we groupby group, and get aggregate number of each groups' total attack times and casued casaulities.


```python
df_terro_group=df.groupby('Group').agg({'Group':'count', 'Total_num':'sum'}).\
rename(columns={'Group':"Times"})
df_terro_group=df_terro_group.reset_index()  
```

We take all terrorism groups into account and get the total number of terrorist attack together with total casualities caused of each group.  These two values noted as 'Times' and 'Total_num'. 


```python
df_terro_group.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Group</th>
      <th>Times</th>
      <th>Total_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 May</td>
      <td>10</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14 K Triad</td>
      <td>4</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14 March Coalition</td>
      <td>1</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14th of December Command</td>
      <td>3</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15th of September Liberation Legion</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16 January Organization for the Liberation of ...</td>
      <td>24</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1920 Revolution Brigades</td>
      <td>2</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>19th of July Christian Resistance Brigade</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1st of May Group</td>
      <td>3</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2 April Group</td>
      <td>6</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



We noticed that some of groups with less attack times really caused huge number of casaulities, whereas some of the other 
groups were quite active (attacked a lot) but with quite small number of wounds and fatalities. 

Referring to this fact, we started to analize finding 1. 

# 1.2 Analysis

## 1.2.1 Data Preperation


### Firstly, plot on the Terrorism Group with number of attack times and total wounds and fatalities

Ranked the terrorist groups by number of wounds and fatalities. 
Found the group with most value is Unkown,which means the dataset did not record the group information of those terrorist attacks 


```python
sns.barplot(x=df_terro_group.Total_num.nlargest(15)[0:15], y=df_terro_group.iloc[df_terro_group.Total_num.nlargest(15)[0:15].index].Group.values,palette=('inferno'))
plt.xticks(rotation=90)
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.title('Terrorist Groups (Rank by Total wounds and fatalities)')
plt.show()

```


![png](output_47_0.png)


After removing the unknown group


```python
sns.barplot(x=df_terro_group.Times.nlargest(15)[1:15], y=df_terro_group.iloc[df_terro_group.Times.nlargest(15)[1:15].index].Group.values,palette=('inferno'))
plt.xticks(rotation=90)
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.title('Terrorist Groups (Rank by attack times)')
```




    Text(0.5,1,u'Terrorist Groups (Rank by attack times)')




![png](output_49_1.png)


The following plot is the groups ranked by number of casualties also excluding the unkown group.
Comparing the groups in these two ranks we noticed that there have some overlaps,they are quite different.(Al qaida which responsible for 911 attack in 2012 US) 
o named these groups 'active' and 'deadliest'


```python
sns.barplot(x=df_terro_group.Total_num.nlargest(15)[1:15], y=df_terro_group.iloc[df_terro_group.Total_num.nlargest(15)[1:15].index].Group.values,palette=('inferno'))
plt.xticks(rotation=90)
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.title('Terrorist Groups (Rank by Total wounds and fatalities)')
plt.show()

```


![png](output_51_0.png)


### Secondly,  Subset Terrorist Groups Based On Two Standards.

Subset one group by attack times, choose top 100. 


```python
##Time Max
index_times_100=df.groupby('Group').size()[df.groupby('Group').size().values!=1].nlargest(100).index
value_times_100=df.groupby('Group').size()[df.groupby('Group').size().values!=1].nlargest(100).values
df_times_100=df[df['Group'].isin(index_times_100)]
```

Subset another group by casulities numbers, choose top 100. 


```python
##Dead Max
index_dead_100=df.groupby('Group').agg({'Total_num':'sum'}).Total_num.nlargest(100).index
values_dead_100=df.groupby('Group').agg({'Total_num':'sum'}).Total_num.nlargest(100).values
df_dead_100=df[df['Group'].isin(index_dead_100)]
```


```python
#df_merge=df0.merge(group_table, how='left')
#df=df_merge[df_merge['Times'].isnull()==False]
#df_final.to_csv('Final_Python1.csv', index=False)
```


```python
group_times_100=pd.DataFrame({'Group_Name':index_times_100, 'Value_Times':value_times_100})
group_dead_100=pd.DataFrame({'Group_Name':index_dead_100, 'values_dead':values_dead_100})
```


```python
group_inner=group_times_100.merge(group_dead_100,how='inner')
group_outer_130=group_times_100.merge(group_dead_100,how='outer')
inner_list=group_inner.Group_Name.values
group_outer_130_list=group_outer_130.Group_Name
group_times_100=group_times_100.set_index(['Group_Name'])
group_dead_100=group_dead_100.set_index(['Group_Name'])
```


```python
df_times_100=df[df['Group'].isin(group_times_100.index)]
df_dead_100=df[df['Group'].isin(group_dead_100.index)]
#df_dead_30.to_csv('dead_30.csv', index=False)
#df_times_30.to_csv('Times_30.csv', index=False)
#df_times_100.to_csv('Times_100.csv', index=False)
#df_dead_100.to_csv('Dead_100.csv', index=False)
#df_group_130=df[df['Group'].isin(group_outer_130_list.index)]group_outer_130_list
#df_group_130.to_csv('group_130.csv', index=False)
```


```python
set1 = set(group_dead_100.index)
set2 = set(group_times_100.index)
venn2([set1, set2], ('Top 100 Deadliest groups', 'Top 100 Active groups'))
fig=plt.gcf()
fig.set_size_inches(18,7)
plt.show()
```


![png](output_61_0.png)


We drew the venn graph of 100 groups from 'active' and 'deadliest' and found that
there are 70 groups overlapping.
So we started with those 30 groups that do not overlap and try to find some interesting findings there.


```python
venn_pic = mpimg.imread('Image003.tif') 
venn_pic.shape
plt.imshow(venn_pic) 
plt.axis('off') 
fig=plt.gcf()
fig.set_size_inches(18,7) 
plt.show()
```


![png](output_63_0.png)


### Thirdly, Found Unexpected 30 Deadliest And Most Active Terrorist Groups

The following code aims to create 3 new dataset which is the 30 Deadliest group, 30 active group and 70 inner group respectively.


```python
#in the Middle 70 groups 
df_groups_70=df[df['Group'].isin(inner_list)]
```


```python
times_max_30=[]
for i in group_times_100.index:
    if i not in inner_list:
        times_max_30.append(i)
```


```python
dead_max_30=[]
for j in group_dead_100.index:
    if j not in inner_list:
        dead_max_30.append(j)
```


```python
times_max=group_times_100.loc[times_max_30]
dead_max=group_dead_100.loc[dead_max_30]
df_times_30=df[df['Group'].isin(times_max.index)]
df_dead_30=df[df['Group'].isin(dead_max.index)]
```


```python
import matplotlib.pyplot as plt
labels=['Deadliest Groups', 'Active Groups']
X=[len(df_dead_30),len(df_times_30)]
colors = ['red', 'yellowgreen']
explode = (0, 0 )
fig = plt.figure() 
plt.pie(X, explode=explode, labels=labels, 
        autopct='%1.1f%%', shadow=True, colors=colors,startangle=140)
plt.axis('equal')
plt.title("Terrorists Pie chart") 
plt.show()
```


![png](output_70_0.png)


We show the percentage of number of terriorist attack of theses 60 groups.
As we can see, the active groups occupy 82.8% of number of attacks


```python
labels=['Deadliest Groups', 'Active Groups']
X=[df_dead_30.Total_num.sum(),df_times_30.Total_num.sum()]
fig = plt.figure()  
colors = ['red', 'yellowgreen']
explode = (0.2, 0 )
fig = plt.figure() 
plt.pie(X, explode=explode, labels=labels, 
        autopct='%1.1f%%', shadow=True, colors=colors,startangle=140)
plt.axis('equal')
plt.title("Killed/wounded number Pie chart") 
plt.show()
# As we can see, the deadliest groups occupy 84.9% of number of death and wound
```


    <matplotlib.figure.Figure at 0x1a397b0590>



![png](output_72_1.png)


As we can see, the deadliest groups occupy 84.9% of number of death and wound

## 1.2.2 Why They Are So Different? 

### A. Regional Difference

We want to figure out the geographic distributions of these three groups.


```python
import matplotlib.patches as mpatches
def draw_group(top_groups,color='r',m4=None):
    if not m4:
        m4 = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c',lat_0=True,lat_1=True)
        m4.drawcoastlines()
        m4.drawcountries()
        m4.fillcontinents(lake_color='grey')
        m4.drawmapboundary(fill_color='grey')
        fig=plt.gcf()
        fig.set_size_inches(22,10)
    group=list(top_groups['Group'].unique())
    for g in group:
        lat_group=list(top_groups[top_groups['Group']==g].latitude)
        long_group=list(top_groups[top_groups['Group']==g].longitude)
        x_group,y_group=m4(long_group,lat_group)
        m4.plot(x_group,y_group,'go',markersize=3,color=color,label=g)
#     legend=plt.legend(loc='lower left',frameon=True,prop={'size':10})
#     frame=legend.get_frame()
#     frame.set_facecolor('white')
#     plt.show()
    return m4

m4=draw_group(df_groups_70,'yellow')
m4=draw_group(df_times_30,'b')
m4=draw_group(df_dead_30,'r')
patch1 = mpatches.Patch(color='b', label='30 Active terrorism groups')
patch2 = mpatches.Patch(color='r', label='30 Deadliest terrorism groups')
patch3 = mpatches.Patch(color='lightyellow', label='70 Inner terrorism groups')
plt.legend(handles=[patch1,patch2,patch3],loc=3)
plt.title('Regional Activities of Terrorist Groups')
plt.show()
```


![png](output_77_0.png)



```python
##Merge into plot
labels=df_dead_30.groupby('Region').size().sort_values(ascending=False).index
X=df_dead_30.groupby('Region').size().sort_values(ascending=False).values
df_labels=pd.DataFrame({'Region':labels, 'Times':X})
df_labels['Ratio']=df_labels.Times*1.0/(df_labels.Times.sum())
labels_2=df_times_30.groupby('Region').size().sort_values(ascending=False).index
X_2=df_times_30.groupby('Region').size().sort_values(ascending=False).values
df_labels_2=pd.DataFrame({'Region':labels_2, 'Times2':X_2})
df_labels_2['Ratio2']=df_labels_2.Times2*1.0/(df_labels_2.Times2.sum())
```


```python
df_labels.merge(df_labels_2,how='inner').drop(columns=['Times','Times2']).\
rename(columns={'Ratio':'Deadliest','Ratio2':'Active Group'}).set_index(keys='Region').plot.bar(width=0.9)
fig=plt.gcf()
fig.set_size_inches(18,7)
plt.title('Regional analysis')
plt.show() 
```


![png](output_79_0.png)


Looking at the map and barplot above, we have the following key findings
1. The 'active' groups are most active in Europe
2. The 'active' groups are more wide spread comparing to the 'deadliest' group
3. The inner groups are more worldwide and distributed on most of the populated regions which is also as expected.

#### Next we will be more focused on the difference between the active and deadliest group.

### B. Motive Perspective

Use the nltk package and wordcloud package to get the keyword of motive


```python
import nltk
from wordcloud import WordCloud
nltk.download('popular')
def gen_word_cloud(series,use_mask=False,save_file_name=None):
    text=series.str.lower().str.replace(r'\|', ' ').str.cat(sep=' ')
    text=text.decode('unicode_escape').encode('ascii','ignore')
    words=nltk.tokenize.word_tokenize(text)
    word_dist = nltk.FreqDist(words)
    stopwords = nltk.corpus.stopwords.words('english')
    if use_mask:
        mask = np.array(Image.open("kaggle.png"))
        width=mask.shape[1]
        height=mask.shape[0]
    else:
        mask=None
        width=1000
        height=1000
    words_except_stop_dist = nltk.FreqDist(w for w in words if w not in stopwords) 
    wordcloud = WordCloud(stopwords=stopwords,max_words=100, background_color='white',mask=mask,
                         width=width, height=height).\
        generate(" ".join(words_except_stop_dist))
    plt.imshow(wordcloud)
    plt.axis("off")
    if save_file_name:
        wordcloud.to_file(save_file_name)
```

    [nltk_data] Downloading collection u'popular'
    [nltk_data]    | 
    [nltk_data]    | Downloading package cmudict to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package cmudict is already up-to-date!
    [nltk_data]    | Downloading package gazetteers to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package gazetteers is already up-to-date!
    [nltk_data]    | Downloading package genesis to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package genesis is already up-to-date!
    [nltk_data]    | Downloading package gutenberg to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package gutenberg is already up-to-date!
    [nltk_data]    | Downloading package inaugural to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package inaugural is already up-to-date!
    [nltk_data]    | Downloading package movie_reviews to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package movie_reviews is already up-to-date!
    [nltk_data]    | Downloading package names to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package names is already up-to-date!
    [nltk_data]    | Downloading package shakespeare to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package shakespeare is already up-to-date!
    [nltk_data]    | Downloading package stopwords to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package stopwords is already up-to-date!
    [nltk_data]    | Downloading package treebank to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package treebank is already up-to-date!
    [nltk_data]    | Downloading package twitter_samples to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package twitter_samples is already up-to-date!
    [nltk_data]    | Downloading package omw to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package omw is already up-to-date!
    [nltk_data]    | Downloading package wordnet to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package wordnet is already up-to-date!
    [nltk_data]    | Downloading package wordnet_ic to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package wordnet_ic is already up-to-date!
    [nltk_data]    | Downloading package words to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package words is already up-to-date!
    [nltk_data]    | Downloading package maxent_ne_chunker to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package maxent_ne_chunker is already up-to-date!
    [nltk_data]    | Downloading package punkt to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package punkt is already up-to-date!
    [nltk_data]    | Downloading package snowball_data to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package snowball_data is already up-to-date!
    [nltk_data]    | Downloading package averaged_perceptron_tagger to
    [nltk_data]    |     /Users/liyuexi/nltk_data...
    [nltk_data]    |   Package averaged_perceptron_tagger is already up-
    [nltk_data]    |       to-date!
    [nltk_data]    | 
    [nltk_data]  Done downloading collection popular


Word cloud picture shows the keyword of 30 Deadliest group


```python
gen_word_cloud(df_dead_30.Motive)
```


![png](output_86_0.png)


Word cloud picture shows the keyword of 30 Active group 


```python
gen_word_cloud(df_times_30.Motive)
```


![png](output_88_0.png)


Comparing to the active group, the motive of the deadliest groups are more about religion and politics

###  C. Weapon Type

This plot shows each weapon type and its corresponding Ratio of using in terrorist attack.


```python
##Merge into plot
labels_w=df_dead_30.groupby('Weapon_type').size().sort_values(ascending=False).index
X_w=df_dead_30.groupby('Weapon_type').size().sort_values(ascending=False).values
df_labels_w=pd.DataFrame({'Weapon_type':labels_w, 'Times':X_w})
df_labels_w['Ratio']=df_labels_w.Times*1.0/(df_labels_w.Times.sum())
labels_2_w=df_times_30.groupby('Weapon_type').size().sort_values(ascending=False).index
X_2_w=df_times_30.groupby('Weapon_type').size().sort_values(ascending=False).values
df_labels_2_w=pd.DataFrame({'Weapon_type':labels_2_w, 'Times2':X_2_w})
df_labels_2_w['Ratio2']=df_labels_2_w.Times2*1.0/(df_labels_2_w.Times2.sum())
```


```python
df_labels_w.merge(df_labels_2_w,how='inner').drop(columns=['Times','Times2']).\
rename(columns={'Ratio':'Deadliest','Ratio2':'Active Group'}).set_index(keys='Weapon_type').plot.bar(width=0.9)
fig=plt.gcf()
fig.set_size_inches(18,7) 
plt.title('WeaponType Analysis')
plt.show() 
```


![png](output_93_0.png)


### D. Attack Type


```python
##Mergeainto plot
labels_a=df_dead_30.groupby('AttackType').size().sort_values(ascending=False).index
X_a=df_dead_30.groupby('AttackType').size().sort_values(ascending=False).values
df_labels_a=pd.DataFrame({'AttackType':labels_a, 'Times':X_a})
df_labels_a['Ratio']=df_labels_a.Times*1.0/(df_labels_a.Times.sum())
labels_2_a=df_times_30.groupby('AttackType').size().sort_values(ascending=False).index
X_2_a=df_times_30.groupby('AttackType').size().sort_values(ascending=False).values
df_labels_2_a=pd.DataFrame({'AttackType':labels_2_a, 'Times2':X_2_a})
df_labels_2_a['Ratio2']=df_labels_2_a.Times2*1.0/(df_labels_2_a.Times2.sum())
```


```python
df_labels_a.merge(df_labels_2_a,how='inner').drop(columns=['Times','Times2']).\
rename(columns={'Ratio':'Deadliest','Ratio2':'Active Group'}).set_index(keys='AttackType').plot.bar(width=0.9)
fig=plt.gcf()
fig.set_size_inches(18,7) 
plt.title('Attack Type analysis')
plt.show() 
```


![png](output_96_0.png)


We can see from the attack type plot and weapon type plot, those two groups did not share much difference, meaning that their ways of conducting terrorist are pretty much the same expect the regional issues and motives.

What else could be the reason behind the scene?

## 1.2.3 Significant Reason: Suicide attack !!!


```python
list_suici_times=[len(df_times_30[df_times_30.suicide==1]),len(df_times_30)]
list_suici_dead=[len(df_dead_30[df_dead_30.suicide==1]),len(df_dead_30)]
```


```python
labels=['Suicide attack', 'Non-suicide attack']
X=list_suici_times
colors = ['red', 'lightblue']
explode = (0.2, 0 )
plt.pie(X, explode=explode, labels=labels, 
        autopct='%1.1f%%', shadow=True, colors=colors,startangle=140)
plt.axis('equal')
plt.title("Suicide attack for Active group")
plt.show()
```


![png](output_101_0.png)



```python
labels=['Suicide attack', 'Non-suicide attack']
X=list_suici_dead
colors = ['red', 'lightblue']
explode = (0.2, 0 )
plt.pie(X, explode=explode, labels=labels, 
        autopct='%1.1f%%', shadow=True, colors=colors,startangle=140)
plt.axis('equal')
plt.title("Suicide attack for Deadliest group") 
plt.show()
```


![png](output_102_0.png)


<li>The interesting difference is that active group rarely conduct suicide attack(0.2%),but deadliest groups conduct rougly 11% of suicide attacks.
<li> How horrible if a terrorist attack is a suicide attack?


```python
all_suici=[df[df.suicide==1].Total_num.sum(),df[df.suicide==0].Total_num.sum()]
part_suici=[df_dead_30[df_dead_30.suicide==1].Total_num.sum(),\
            df_dead_30[df_dead_30.suicide==0].Total_num.sum()]
```


```python
labels=['Deadlist Group suicide', 'Non suicide']
X=part_suici
fig = plt.figure().set_size_inches(6,6) 
plt.pie(X,labels=labels,autopct='%1.2f%%')
plt.title("Suicide attack for Deadlist group") 
```




    Text(0.5,1,u'Suicide attack for Deadlist group')




![png](output_105_1.png)


Although suicide attack only accounts for nearly 10% from those deadliest groups, it caused 55.66% of deadth and wounds. 

# 1.3 Conclusion:

<li> Although at frist we hope to find something different in regards to the weapon type and attack type of these two kind of groups, 
unexpectly the results show their way of attack and attack weapon are quite similar. 
<li> When we looked into the dataset and digged from the information recorded of the terrorism attacks,we found the most horrible,bloody and extreme attack is depends on the attack-motive---an attack is whether conducted in a suicide way. 

##  ------------------------------------------------Finding 2-------------------------------------------------

# Finding 2 : Why Terrorism in Western Europe Brought Low Causualties?

# 2.1 Assumption

Is casualties in each time attack balanced in world wide? We assume developed countries may have low time and casuality ration. So first we did a small calculation to test the assumption.


```python
df_raw = pd.read_csv('group_130.csv')
```


```python
df_raw.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Country</th>
      <th>Region</th>
      <th>city</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>AttackType</th>
      <th>Killed</th>
      <th>...</th>
      <th>Sub_Target</th>
      <th>success</th>
      <th>suicide</th>
      <th>Weapon_type</th>
      <th>Sub_Weapon_type</th>
      <th>Motive</th>
      <th>Summary</th>
      <th>addnotes</th>
      <th>Total_num</th>
      <th>casualities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1970</td>
      <td>1</td>
      <td>2</td>
      <td>United States</td>
      <td>North America</td>
      <td>Oakland</td>
      <td>37.805065</td>
      <td>-122.273024</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>Electricity</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>1/2/1970: Unknown perpetrators detonated explo...</td>
      <td>Damages were estimated to be between $20,000-$...</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1970</td>
      <td>1</td>
      <td>6</td>
      <td>United States</td>
      <td>North America</td>
      <td>Denver</td>
      <td>39.740010</td>
      <td>-104.992259</td>
      <td>Facility/Infrastructure Attack</td>
      <td>0.0</td>
      <td>...</td>
      <td>Military Recruiting Station/Academy</td>
      <td>1</td>
      <td>0</td>
      <td>Incendiary</td>
      <td>Molotov Cocktail/Petrol Bomb</td>
      <td>Protest the draft and Vietnam War</td>
      <td>1/6/1970: Unknown perpetrators threw a Molotov...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1970</td>
      <td>1</td>
      <td>8</td>
      <td>Italy</td>
      <td>Western Europe</td>
      <td>Rome</td>
      <td>41.890520</td>
      <td>12.494249</td>
      <td>Hijacking</td>
      <td>0.0</td>
      <td>...</td>
      <td>Aircraft (not at an airport)</td>
      <td>1</td>
      <td>0</td>
      <td>Firearms</td>
      <td>Rifle/Shotgun (non-automatic)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1970</td>
      <td>1</td>
      <td>9</td>
      <td>United States</td>
      <td>North America</td>
      <td>Detroit</td>
      <td>42.331685</td>
      <td>-83.047924</td>
      <td>Facility/Infrastructure Attack</td>
      <td>0.0</td>
      <td>...</td>
      <td>Government Building/Facility/Office</td>
      <td>1</td>
      <td>0</td>
      <td>Incendiary</td>
      <td>Molotov Cocktail/Petrol Bomb</td>
      <td>NaN</td>
      <td>1/9/1970: Unknown perpetrators set off a fireb...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1970</td>
      <td>1</td>
      <td>20</td>
      <td>Guatemala</td>
      <td>Central America &amp; Caribbean</td>
      <td>Guatemala City</td>
      <td>14.624422</td>
      <td>-90.532880</td>
      <td>Assassination</td>
      <td>1.0</td>
      <td>...</td>
      <td>Embassy/Consulate</td>
      <td>1</td>
      <td>0</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>




```python
df_2=df_raw.groupby('Region').agg({'Region':'count', 'Total_num':'sum'}).rename(columns={'Region':'Times'})
```


```python
df_2['Time_Casuality_ratio'] = df_2['Total_num']/df_2['Times']
```


```python
df_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Times</th>
      <th>Total_num</th>
      <th>Time_Casuality_ratio</th>
    </tr>
    <tr>
      <th>Region</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Australasia &amp; Oceania</th>
      <td>174</td>
      <td>193.0</td>
      <td>1.109195</td>
    </tr>
    <tr>
      <th>Central America &amp; Caribbean</th>
      <td>8911</td>
      <td>31141.0</td>
      <td>3.494670</td>
    </tr>
    <tr>
      <th>Central Asia</th>
      <td>461</td>
      <td>2466.0</td>
      <td>5.349241</td>
    </tr>
    <tr>
      <th>East Asia</th>
      <td>555</td>
      <td>9378.0</td>
      <td>16.897297</td>
    </tr>
    <tr>
      <th>Eastern Europe</th>
      <td>4602</td>
      <td>16112.0</td>
      <td>3.501086</td>
    </tr>
    <tr>
      <th>Middle East &amp; North Africa</th>
      <td>43127</td>
      <td>289184.0</td>
      <td>6.705405</td>
    </tr>
    <tr>
      <th>North America</th>
      <td>1353</td>
      <td>21545.0</td>
      <td>15.923873</td>
    </tr>
    <tr>
      <th>South America</th>
      <td>16919</td>
      <td>39330.0</td>
      <td>2.324605</td>
    </tr>
    <tr>
      <th>South Asia</th>
      <td>37415</td>
      <td>193930.0</td>
      <td>5.183215</td>
    </tr>
    <tr>
      <th>Southeast Asia</th>
      <td>10391</td>
      <td>34069.0</td>
      <td>3.278703</td>
    </tr>
    <tr>
      <th>Sub-Saharan Africa</th>
      <td>13106</td>
      <td>81408.0</td>
      <td>6.211506</td>
    </tr>
    <tr>
      <th>Western Europe</th>
      <td>12174</td>
      <td>17540.0</td>
      <td>1.440775</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_bar=pd.DataFrame({'bar': df_2.index, 'bar_val':df_2['Time_Casuality_ratio']}).sort_values(by = ['bar_val'])
```


```python
sns.factorplot(y='bar',x='bar_val',data=df_bar,kind='bar',aspect=5)
```




    <seaborn.axisgrid.FacetGrid at 0x1a482b2390>




![png](output_119_1.png)


Through the histogram above, we found quite suprised result. Not all developed countries have low ration. The first one is Australasia and oceania area, while considering its low attack time happened in last 50 years, we didn't keep study on it. We then found the second one is Western Europe, which owns 1.4 ration and had ten thousand times more attack in the pass. Compare to that, north america has ratio of 15. So we decided to study on Western Europe to see why this happened.

# 2.2 Analysis 

## 2.2.1 Usual Weapon/Attack Type And Casualties

First, we decided to draw a decision tree to see which factor affect most. And we use casualities, which means whether the attack succeed or not as our dependent variable.


```python
dtree = df_raw.drop(columns = ['Day','Month','city','latitude','longitude','Killed','Wounded','Sub_Target','success','suicide','Motive'
                             ,'Summary','addnotes','Total_num'])
```


```python
dt = tree.DecisionTreeClassifier(max_depth=2)
```


```python
WEur = dtree[dtree['Region'] == 'Western Europe']
```


```python
WEur = WEur.dropna()
WEur.drop('Region',axis = 1, inplace = True)
```


```python
len(WEur)
```




    10239




```python
WEur = pd.get_dummies(WEur, columns = ['Country','AttackType','Group','Target_type',
                                  'Weapon_type','Sub_Weapon_type'],dummy_na=True)
```


```python
X = WEur.drop('casualities',axis=1)
Y = WEur.casualities
dt.fit(X,Y)
```




    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=2,
                max_features=None, max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, presort=False, random_state=None,
                splitter='best')




```python
dt_feature_names = list(X.columns)
dt_target_names = np.array(Y.unique(),dtype=np.string_) 
tree.export_graphviz(dt, out_file='tree.dot', 
    feature_names=dt_feature_names, class_names=dt_target_names,
    filled=True)  
graph = pydotplus.graph_from_dot_file('tree.dot')
Image(graph.create_png())
```




![png](output_131_0.png)



Here, we found the most easily type can kill a western european are using handgun, automatic weapon and assassination. However, are these three type can lead heavy casualties? So we drawn a heatmap.


```python
z = df_raw[df_raw['Region'] == 'Western Europe']
zz = z.groupby(['Sub_Weapon_type','AttackType'])['Total_num'].sum()
sns.heatmap(zz.unstack(),annot=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1a352fdbd0>




![png](output_133_1.png)


From the heatmap, we found those three type didn't lead to heavy casualties. In another word, the most easilest succeed three way in Western Europe actually lead low casualities. 
Then which attack type and weapon type are most favored by terrorists? 


```python
df_bar=z.groupby('Sub_Weapon_type').size().sort_values(ascending=False)
df_bar=pd.DataFrame({'bar': df_bar.index, 'bar_val':df_bar.values})
sns.factorplot(y='bar',x='bar_val',data=df_bar,kind='bar',aspect=6)
```




    <seaborn.axisgrid.FacetGrid at 0x1a3b04d6d0>




![png](output_135_1.png)



```python
df_bar=z.groupby('AttackType').size().sort_values(ascending=False)
df_bar=pd.DataFrame({'bar': df_bar.index, 'bar_val':df_bar.values})
sns.factorplot(y='bar',x='bar_val',data=df_bar,kind='bar',aspect=6)
```




    <seaborn.axisgrid.FacetGrid at 0x1a3b04df10>




![png](output_136_1.png)


We can see the most type choosen by terrorist in Western Europs is Explosive and bombing, which is hard succeed in Europe, however, seen from the decision tree. We own to the strict regulation by government. 

## 2.2.2 Most Active Group

Also, from the region distribution in finding one, we found another reason that lead the low casualities in Western Europe.


```python
df_30 = pd.read_csv('Times_30.csv')
```


```python
len(df_30[df_30['Region'] == 'Western Europe'])/float(len(df_30))
```




    0.31353951890034365




```python
m4=draw_group(df_times_30,'b')
m4=draw_group(df_dead_30,'r')
patch1 = mpatches.Patch(color='b', label='30 Active terrorism groups')
patch2 = mpatches.Patch(color='r', label='30 Deadliest terrorism groups')
plt.legend(handles=[patch1,patch2,patch3],loc=3)
plt.title('Regional Activities of Terrorist Groups')
plt.show()

```


![png](output_142_0.png)


From the map above, we can see the 30 active terrorism groups love attack Western Europe. We think this attribute some to the low casualities in Western Europe. Also, we drawn a bar chart below to show it more clearly. 


```python
df_bar=df_30.groupby('Region').size().sort_values(ascending=False)
df_bar=pd.DataFrame({'bar': df_bar.index, 'bar_val':df_bar.values})
sns.factorplot(y='bar_val',x='bar',data=df_bar,kind='bar',aspect=6)
```




    <seaborn.axisgrid.FacetGrid at 0x1a18bbbdd0>




![png](output_144_1.png)


# 2.3 Conclusion

Therefore, we have to reason to explain the low casualities in Western Europe. First is the most easy way lead to attack success has few casualities which explain the low casualities and the most way used by terrorists is hard to succeed which explains the high attack time. Second reason is the 30 active groups, they lead both high attack time and low casualities to Western Europe.

## ------------------------------------------------Finding 3-------------------------------------------------

# Finding 3 : Are Oil or Gas Primary Targets for Terrorists? NO!

After we retrieved all of the data of Middle East & North Africa region as a sub dataset and found that anti-regime and combating for religious differences are their main reasonsfor attacks.

# 3.1 Assumption：

Generally, we assume that oil and gas are a big reason behind terrorism and and some terrorist groups are even reported that after they occupied the oil production area, they might trade them in black market for money to support themselves.

## 3.1.1: Number Of Terrorist Activities By Region

From our dataset, at first glance, it seems so. Especially when we aggregate the number of terrorist activities and casualties by region, we would find that across the world, Middle East & North Africa, which is also the well-known oil production region, is the most attacked region and also lost much more casualties among 12 regions. 


```python
plt.subplots(figsize=(15,6))
sns.countplot('Region',data=df,palette='RdYlGn',edgecolor=sns.color_palette('dark',7),order=df['Region'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Number Of Terrorist Activities By Region')
plt.show()
```


![png](output_154_0.png)


## 3.1.2: Number Of Terrorism Casualties By Region


```python
df_bar=df.groupby('Region')['Total_num'].sum().sort_values(ascending=False)
df_bar=pd.DataFrame({'Region': df_bar.index, 'Total_num':df_bar.values})
sns.factorplot(y='Region',x='Total_num',data=df_bar,kind='bar',aspect=6)
```




    <seaborn.axisgrid.FacetGrid at 0x1a18bd6810>




![png](output_156_1.png)


## 3.1.3: Top 16 Attacked Countries in Middle East & North Africa


And if we further look at this region by country, in this data set, there are 23 countries from this area. Top affected 16 countries in Middle East & North Africa are mainly oil production countries. 



```python
Region_MiddleEast = df[df.Region == 'Middle East & North Africa']
Region_MiddleEast.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Country</th>
      <th>Region</th>
      <th>city</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>AttackType</th>
      <th>Killed</th>
      <th>...</th>
      <th>Sub_Target_type</th>
      <th>success</th>
      <th>suicide</th>
      <th>Weapon_type</th>
      <th>Sub_Weapon_type</th>
      <th>Motive</th>
      <th>Summary</th>
      <th>addnotes</th>
      <th>Total_num</th>
      <th>casualities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>95</th>
      <td>1970</td>
      <td>2</td>
      <td>28</td>
      <td>Jordan</td>
      <td>Middle East &amp; North Africa</td>
      <td>Hebron</td>
      <td>31.532521</td>
      <td>35.100248</td>
      <td>Armed Assault</td>
      <td>NaN</td>
      <td>...</td>
      <td>Tour Bus/Van</td>
      <td>1</td>
      <td>0</td>
      <td>Firearms</td>
      <td>Automatic Weapon</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>133</th>
      <td>1970</td>
      <td>3</td>
      <td>14</td>
      <td>Egypt</td>
      <td>Middle East &amp; North Africa</td>
      <td>Alexandria</td>
      <td>31.198056</td>
      <td>29.919167</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>Aircraft (not at an airport)</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>158</th>
      <td>1970</td>
      <td>3</td>
      <td>29</td>
      <td>Lebanon</td>
      <td>Middle East &amp; North Africa</td>
      <td>Beirut</td>
      <td>33.888629</td>
      <td>35.495479</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>Embassy/Consulate</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>195</th>
      <td>1970</td>
      <td>4</td>
      <td>15</td>
      <td>Jordan</td>
      <td>Middle East &amp; North Africa</td>
      <td>Amman</td>
      <td>31.950001</td>
      <td>35.933331</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>Embassy/Consulate</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>226</th>
      <td>1970</td>
      <td>4</td>
      <td>25</td>
      <td>Turkey</td>
      <td>Middle East &amp; North Africa</td>
      <td>Istanbul</td>
      <td>41.014836</td>
      <td>28.961414</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>Airline Officer/Personnel</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>




```python
plt.subplots(figsize=(18,6))
sns.barplot(Region_MiddleEast['Country'].value_counts()[:16].index,Region_MiddleEast['Country'].value_counts()[:16].values,palette='inferno')
plt.title('Top 16 Attacked Countries in Middle East & North Africa')
plt.show()
```


![png](output_160_0.png)


## 3.1.4: Global Oil Ranking of Most Affected Countries in Middle East & North Africa

If we compare them with global oil producing ranking, 47% of them are among Top 50 oil producing countries. 


```python
oil = pd.read_csv('Oil_Country.csv')
oil = oil.drop(['Unnamed: 0'],axis = 1)
```


```python
oil.Country=oil.Country.apply(lambda x : x.decode('unicode_escape').encode('ascii','ignore'))
```


```python
oil.columns.unique()
```




    Index([u'Rank', u'Country'], dtype='object')




```python
Oil_rank = Region_MiddleEast.merge(oil, left_on='Country', right_on='Country',how = 'left')
```


```python
Oil_rank.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Country</th>
      <th>Region</th>
      <th>city</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>AttackType</th>
      <th>Killed</th>
      <th>...</th>
      <th>success</th>
      <th>suicide</th>
      <th>Weapon_type</th>
      <th>Sub_Weapon_type</th>
      <th>Motive</th>
      <th>Summary</th>
      <th>addnotes</th>
      <th>Total_num</th>
      <th>casualities</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1970</td>
      <td>2</td>
      <td>28</td>
      <td>Jordan</td>
      <td>Middle East &amp; North Africa</td>
      <td>Hebron</td>
      <td>31.532521</td>
      <td>35.100248</td>
      <td>Armed Assault</td>
      <td>NaN</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>Firearms</td>
      <td>Automatic Weapon</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1970</td>
      <td>3</td>
      <td>14</td>
      <td>Egypt</td>
      <td>Middle East &amp; North Africa</td>
      <td>Alexandria</td>
      <td>31.198056</td>
      <td>29.919167</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1970</td>
      <td>3</td>
      <td>29</td>
      <td>Lebanon</td>
      <td>Middle East &amp; North Africa</td>
      <td>Beirut</td>
      <td>33.888629</td>
      <td>35.495479</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
      <td>151.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1970</td>
      <td>4</td>
      <td>15</td>
      <td>Jordan</td>
      <td>Middle East &amp; North Africa</td>
      <td>Amman</td>
      <td>31.950001</td>
      <td>35.933331</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1970</td>
      <td>4</td>
      <td>25</td>
      <td>Turkey</td>
      <td>Middle East &amp; North Africa</td>
      <td>Istanbul</td>
      <td>41.014836</td>
      <td>28.961414</td>
      <td>Bombing/Explosion</td>
      <td>0.0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>Explosives/Bombs/Dynamite</td>
      <td>Unknown Explosive Type</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0</td>
      <td>54.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>




```python
ME_rank = Oil_rank[['Country','Rank']].drop_duplicates()
ME_rank.sort_values(by = ['Rank'],ascending = True).set_index(keys=[range(0,len(ME_rank))]).drop(0,axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Iran</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iraq</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kuwait</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>United Arab Emirates</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Libya</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Qatar</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Algeria</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Egypt</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Yemen</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Syria</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Tunisia</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Turkey</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Bahrain</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Israel</td>
      <td>89.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Jordan</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Morocco</td>
      <td>97.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Lebanon</td>
      <td>151.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Western Sahara</td>
      <td>202.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>South Yemen</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>West Bank and Gaza Strip</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>North Yemen</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>International</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
(len(ME_rank[ME_rank.Rank <= 50])+0.0)*100/len(ME_rank)
```




    47.82608695652174



And even 60% of them are OPEC member countries.


```python
OPEC=[
'Algeria',
'Angola',
'Ecuador',
'Equatorial Guinea',
'Gabon',
'Iran',
'Iraq',
'Kuwait',
'Libya',
'Nigeria',
'Qatar',
'Saudi Arabia',
'United Arab Emirates',
'Venezuela']
opec_country=pd.DataFrame({'Country':OPEC, 'Region_null':OPEC}).set_index(keys=[range(0,len(OPEC))]).drop(0,axis=0)
Count_opec=[]
for country in Region_MiddleEast.Country:
    if country in OPEC:
        Count_opec.append(country)
        
list_region_null=[]
for country in opec_country.Country:
    region_null=df[df.Country==country].Region.values[0]
    list_region_null.append(region_null)
opec_country.Region_null=list_region_null
label_opec=opec_country.groupby('Region_null').count().index
X_opec=[7,4,2]
fig = plt.figure()  
fig.set_size_inches(8,8) 
plt.pie(X_opec,labels=label_opec,autopct='%1.2f%%')
plt.title("OPEC country ratio")
```




    Text(0.5,1,u'OPEC country ratio')




![png](output_171_1.png)


But if we deep into the data, we will found this is not the whole story! 

Maybe Middle East & North Africa is indeed he main area for oil production in the world. But oil and gas are not the main intention for terrorist groups to plot an attack there. Then what are their primary targets for terrorism?

# 3.2 Analysis：




Firstly, from the point view of the target type, the number of business type as a target which including the oil or gas attack is only ranked no.5 of 30 types and the first four are Private Citizens & Property (13929), Military (8215), Police (6531), Government (General) (4090), Business (3879). 

## 3.2.1 : Target type for Middle East & North Africa

According to their target type and sub target type, we found their main target type are still government, military and private citizen. Business reason are secondary.
(Because Terrorist attacking on oil infrastructure is mainly to weaken economies, undermine the authority of governments and exploit local grievances.”)



```python
Region_MiddleEast.groupby('Target_type')['Country'].count().sort_values(ascending  = False)
```




    Target_type
    Private Citizens & Property       13890
    Military                           8185
    Police                             6518
    Government (General)               4075
    Business                           3863
    Unknown                            1626
    Terrorists/Non-State Militia       1606
    Religious Figures/Institutions     1218
    Transportation                     1159
    Government (Diplomatic)             778
    Educational Institution             777
    Utilities                           762
    Journalists & Media                 640
    Violent Political Party             373
    Airports & Aircraft                 272
    Other                               186
    Tourists                            136
    NGO                                 118
    Telecommunication                    70
    Maritime                             53
    Food or Water Supply                 49
    Name: Country, dtype: int64




```python
df_target=Region_MiddleEast.groupby('Target_type')['Country'].count().sort_values(ascending  = False)
df_target=pd.DataFrame({'target_index': df_target.index, 'target_val':df_target.values})
sns.factorplot(y='target_val',x='target_index',data=df_target,kind='bar',aspect=21)
```




    <seaborn.axisgrid.FacetGrid at 0x1a3e6dc750>




![png](output_180_1.png)


## 3.2.2 : Sub Target Type for Middle East & North Africa

Secondly, if we see from sub target type which represents the specific targets for each broad target type, we found that oil or gas as a sub target type are out of 30 and still the first three are all about citizen, government and military including Unnamed Civilian/Unspecified (4820), Police Security Forces/ Officers (3192), Military Personnel (soldiers, troops, officers, forces) (2863), Military Unit/Patrol/Convoy (1999).



```python
index1=Region_MiddleEast.groupby('Sub_Target_type')['Country'].count().sort_values(ascending  = False).rank().index
```


```python
Region_MiddleEast.groupby('Sub_Target_type')['Country'].count().sort_values(ascending  = False).head(35)
```




    Sub_Target_type
    Unnamed Civilian/Unspecified                                               4806
    Police Security Forces/Officers                                            3185
    Military Personnel (soldiers, troops, officers, forces)                    2851
    Military Unit/Patrol/Convoy                                                1990
    Village/City/Town/Suburb                                                   1822
    Government Personnel (excluding police, military)                          1684
    Police Patrol (including vehicles and convoys)                             1557
    Military Barracks/Base/Headquarters/Checkpost                              1398
    Marketplace/Plaza/Square                                                   1354
    Non-State Militia                                                          1346
    Retail/Grocery/Bakery                                                      1112
    House/Apartment/Residence                                                  1090
    Military Checkpoint                                                        1039
    Police Building (headquarters, station, school)                             991
    Politician or Political Party Movement/Meeting/Rally                        900
    Race/Ethnicity Identified                                                   861
    Vehicles/Transportation                                                     826
    Place of Worship                                                            747
    Government Building/Facility/Office                                         714
    Police Checkpoint                                                           687
    Restaurant/Bar/Caf�                                                         682
    Bus (excluding tourists)                                                    622
    Military Transportation/Vehicle (excluding convoys)                         591
    Laborer (General)/Occupation Identified                                     589
    Religion Identified                                                         565
    Named Civilian                                                              501
    School/University/Educational Building                                      471
    Bank/Commerce                                                               395
    Embassy/Consulate                                                           370
    Political Party Member/Rally                                                355
    Public Area (garden, parking lot, garage, beach, public building, camp)     353
    Religious Figure                                                            338
    Newspaper Journalist/Staff/Facility                                         330
    Oil                                                                         324
    Electricity                                                                 309
    Name: Country, dtype: int64




```python
value=Region_MiddleEast.groupby('Sub_Target_type')['Country'].count().sort_values(ascending  = False).rank().values
```


```python
df_get_rank=pd.DataFrame({'index1':index1,'value':value})
```


```python
df_get_rank[df_get_rank.index1 == 'Gas/Oil']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index1</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35</th>
      <td>Gas/Oil</td>
      <td>73.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_sub_target=Region_MiddleEast.groupby('Sub_Target_type')['Country'].count().sort_values(ascending  = False).head(20)
df_sub_target=pd.DataFrame({'sub_target_index': df_sub_target.index, 'sub_target_val':df_sub_target.values})
sns.factorplot(y='sub_target_val',x='sub_target_index',data=df_sub_target,kind='bar',aspect=20)
```




    <seaborn.axisgrid.FacetGrid at 0x1a41017bd0>




![png](output_188_1.png)


## 3.2.3 : Motives by Wordcloud Reflect Religious And Political Appeals

Thirdly, we analyzed from the motive of terrorism. And the following are two word cloud pics made from the most frequent word the terrorist groups use to declare their intention openly to the rest of the world every time for an attack. 


This one just explains even for those terrorists who are directly targeting oil and gas, their motives are more about nation, government and president, which are inclined to be political appeals. 


```python
import matplotlib.image as mpimg
pi_c = mpimg.imread('oil_movtive.png') 
pi_c.shape
plt.imshow(pi_c) 
plt.axis('off') 
fig=plt.gcf()
fig.set_size_inches(20,10) 
plt.show()
```


![png](output_192_0.png)


And this one illustrates those attacks what are targeting religious institutes and figures are more about different religious denomination.



```python
import matplotlib.image as mpimg
pi_c = mpimg.imread('religion_movtive.png') 
pi_c.shape
plt.imshow(pi_c) 
plt.axis('off') 
fig=plt.gcf()
fig.set_size_inches(20,10) 
plt.show()
```


![png](output_194_0.png)


# 3.3 Conclusion:

Therefore, back to our finding, from this dataset we could say that oil or gas are actually not the priorities for terrorists to plot attacks in Middle East and North Africa, governments and religious places are their primary targets.  

In one word, terrorism are more about politics and religion instead of economy. And this can also answer the question we brought at the beginning that why economic condition improved, terrorism instead penetrated more globally. Because their priorities are politics and religion not economy.


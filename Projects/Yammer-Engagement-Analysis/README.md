# Yammer User Engagement Analysis  
## Overview
Yammer is a social network for communicating with coworkers. Individuals share documents, updates, and ideas by posting them in groups. Yammer is free to use indefinitely, but companies must pay license fees if they want access to administrative controls, including integration with user management systems like ActiveDirectory.  
**Problem** :The user engagement started to drop from August 2014.     
**Project Purpose**:Figure out the root cause of the drop in user engagement.     


The [jupyter notebook]() file consists of the following sections. The jupyter file is also available to view in [NBviewer]():   
  
## Table of Content in Jupyter notebook:
&#8195; 1. Libraries and Dependencies

&#8195; 2. Datasets

&#8195; 3. Analysis

&#8195; &#8195; &#8195;  3.1. Weekly Users Engagement

&#8195; &#8195; &#8195;  3.2. Cohort Analysis: Engagement by Users' Signup Age Group

&#8195; &#8195; &#8195;  3.3. Engagement by Device Categories Analysis

&#8195; &#8195; &#8195;  3.4. Email Analysis

&#8195; &#8195; &#8195;  3.5. Signup Process Analysis

&#8195; 4. Reference

### Data 
This project used the fake Yammer datasets , which are available in Mode. And you can check the four sample datasets [**Here**](http://nbviewer.jupyter.org/github/YuexiSC/business-and-data-analytics/blob/master/Projects/Yammer-Engagement-Analysis/Dataset_overview.ipynb).  

|Table | Number of Entries |Features |Explanation|
|--|--|--|--|
| `Users` |19,066   | user_id	|A unique ID per user| 
|||created_at	|The time the user was created(first singed up)|
|||company_id	|The ID of the user's company|
|||language	|The chosen language of the user|
|||activated_at|	The time the user was activated, if they are active|
|||state	|The state of the user (active or pending)| |
|`Events` | 340,832| user_id	|A unique ID per user, which is the ID the user logging the event|
|||occurred_at|	The time the event occurred|
|||event_type|	The general event type|
|||event name	|The specific action the user took|
|||location	|The country from which the event was logged|
|||device	|The type of device used to log the event|
| `Email Events` | 90,389| user_id |	The ID of the user to whom the event relates. Can be joined to user_id in either of the other tables|
|||occurred_at|	The time the event occurred|
|||action|The name of the event that occurred. "sent_weekly_digest" means that the user was delivered a digest email showing relevant conversations from the previous day. "email_open" means that the user opened the email. "email_clickthrough" means that the user clicked a link in the email| 


### Tech Stacks
The project is written in Python 3.6 with Jupyter notebook. I used `pandas` and `numpy` for data analysis, and used `seaborn`, `plotly` for data visualization.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
from datetime import datetime, date
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import seaborn as sns
from __future__ import division
 ```

## Highlights 
The highlighted findings with plots from jupyter notebook are as follows: 

### 1. Weekly Users Engagement   
*Get oriented on how the trend of weekly user engagement looks like*  
<div>
    <a href="https://plot.ly/~yuexili/10/?share_key=TKsFalWnD6DtNBdQQv1w9o" target="_blank" title="Plot 10" style="display: block; text-align: center;"><img src="https://plot.ly/~yuexili/10.png?share_key=TKsFalWnD6DtNBdQQv1w9o" alt="Plot 10" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
   

> The above chart shows the number of engaged users each week. Yammer defines *engagement* as having made some type of server call by interacting with the product (shown in the data as events of type “engagement”). Any point in this chart can be interpreted as “the number of users who logged at least one engagement event during the week starting on that date.” 
> We can see from the graph above, `Aug-3-2014` experienced a drop in the number of active users.    



### 2. Engagement by Device Categories Analysis  
*Check on various device types to see if the problem is localized to any particular product.*    
 
>`all users` means the engagement from all  actual users not the devices they use, that means, if a user has multiple devices, they only count as one. So the total number of `all users` is smaller than all the sum of devices.  
>  If we filter the above chart down to phones (double-click the dot next to “phone” in the legend), we can see that there’s a pretty steep drop in phone engagement rates.   
> So it’s likely that there’s a problem with **the mobile app related to new signed up user retention**. 



### 3. Cohort Analysis: Engagement by Users' Signup Age Group    
*Look at this is to cohort users based on when they signed up for the product to identify the problem whether comes from old users as opposed to new ones.*  

> The `old users` are defined as users who signed up 10 weeks before Sep 1, which is June 22. And the `new users` are the ones who signed up after that. 10 weeks are a empirical value I chose because we want to separate users around the time user engagement decrease happens.

> The graph shows the trend of engagement from old users (signed up more than 10 weeks), new users, as well as all users. We can see that the trend of *old users engagement* drops steadily from mid June. However, we could see that there was a drop in the trend of *new users engagement* round Aug 10, which coincides with the drop of *all user engegament* at that time as well as all the time afterwards.  

> So we can conclude that the drop of engagement probably comes from new signed up users. 


### 4. Signup Process Analysis    
*To visualize each process and to see the conversion rate more easily and precise by using funnel chart.*  

> From `create user` to `enter email`, there are huge amount loss!  And it is the most critical one among all steps, once user entered their email, there is a very large possibility for them to fulfill the following sign-up flows.  
> With this finding, I want to check wether this problem is on device types. So I generated the following segmented funnel chart.  


> The dark green stands for the device computer,  red stands for the device phone and the dark blue is for tablet. 
From step1(`create_user`) to step2(`enter_email`),nearly 40% of users did not go through the second step!  
> From the graph, we can see that all types of devices experienced lost between first and second step. However, computer is the one that suffers the most. So making more user friendly email enter portals can be a good way to attract computer users to get to the second step.  

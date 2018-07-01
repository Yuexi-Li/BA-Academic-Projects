# Global-Terrorism-Analysis
The detail of the implementation can be found here in this [Jupyter Notebook](./Global-Terrorism-Analysis.ipynb)

## Overview 
This project tries to find some interesting findings about global terrorism in a Kaggle dataset [Global Terrorism Database](https://www.kaggle.com/START-UMD/gtd), which records more than 170,000 terrorist attacks worldwide in 1970-2016.   

I use `Pandas`, `Numpy` to manipulating data such as cleaning, grouping and subsetting. `sklearn` are used to analyze the three most easily type of attack which can lead to heavy casualties.  To extract the keywords from the dataset, I use  `nltk`  and `wordcloud` packages.  And then I utilize `matplotlib` and `Seaborn` to visualize the results.
 

The unexpected findings are:
1. The differences between deadliest terrorists groups, who caused most dead and wood, and most active terrorists groups, who caused most attacks, are not in the weapons they used or the places they attacked. In fact, what made the deadliest groups so deadly is that they like to conduct suicide attacks.

2. Terrorists' goals are not economic benefits, such as oil and gas, but governments and religions. This explains why the economy grew in terrorists' homeland but terrorism spread globally.





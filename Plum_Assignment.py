#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


import pandas as pd
df=pd.read_csv('V:/assignment.csv')


# In[7]:


df.head()


# In[8]:


# Group by 'Group' column and calculate average resolution time and number of tickets closed
group_stats = df.groupby('Group').agg({'Resolution time': 'mean', 'Requester id': 'count'})

# Calculate efficiency by dividing number of tickets closed by average resolution time
group_stats['Efficiency'] = group_stats['Requester id'] / group_stats['Resolution time']

# Sort groups by efficiency in descending order
group_stats = group_stats.sort_values(by='Efficiency', ascending=False)

print(group_stats)


# In[9]:


# Plotting the bar chart
plt.figure(figsize=(5, 4))
group_stats['Efficiency'].plot(kind='bar', color='skyblue')
plt.title('Efficiency by Group')
plt.xlabel('Group')
plt.ylabel('Efficiency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[10]:


average_efficiency = group_stats['Efficiency'].mean()
average_efficiency


# In[11]:


# Identify quick and slow groups
quick_groups = group_stats[group_stats['Efficiency'] > average_efficiency]
slow_groups = group_stats[group_stats['Efficiency'] < average_efficiency]

# Create a table showing the efficiency numbers for each group
print("Efficiency Numbers for Each Group:")
print(group_stats)




# In[12]:


# Create a bar chart to visualize the efficiency of each group
plt.figure(figsize=(5, 4))
plt.bar(group_stats.index, group_stats['Efficiency'], color=['green' if eff > average_efficiency else 'red' for eff in group_stats['Efficiency']])
plt.axhline(y=average_efficiency, color='b', linestyle='--', label='Average Efficiency')
plt.xlabel('Group')
plt.ylabel('Efficiency')
plt.title('Efficiency of Each Group')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# In[13]:


# Group tickets by their type and calculate average resolution time
avg_resolution_time = df.groupby('Via')['Resolution time'].mean().reset_index()

avg_resolution_time


# In[14]:


average_resolution_time=avg_resolution_time['Resolution time'].mean()
average_resolution_time


# In[15]:


# Create a table showing the average resolution time for each Via
print("Average Resolution Time for Each Via:")

print(avg_resolution_time)

# Create a bar chart to visualize the average resolution time for each Via
plt.figure(figsize=(6, 4))
plt.bar(avg_resolution_time['Via'], avg_resolution_time['Resolution time'], color=['green' if time > average_resolution_time else 'red' for time in avg_resolution_time['Resolution time']])
plt.axhline(y=average_resolution_time, color='b', linestyle='--', label='Average resolution time')
plt.xlabel('Via')
plt.ylabel('Average Resolution Time (in hr)')
plt.title('Average Resolution Time for Each Via')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





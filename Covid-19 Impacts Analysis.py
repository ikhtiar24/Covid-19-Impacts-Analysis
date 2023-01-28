#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("transformed_data.csv")
data2 = pd.read_csv("raw_data.csv")
print(data)


# In[4]:


print(data.head())


# In[5]:


data["COUNTRY"].value_counts()


# In[6]:


data["COUNTRY"].value_counts().mode()


# In[7]:


code = data["CODE"].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data2.loc[data2["location"] == i, "total_cases"]).sum())
    td.append((data2.loc[data2["location"] == i, "total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data2.loc[data2["location"] == i, "population"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                               columns = ["Country Code", "Country", "HDI", 
                                          "Total Cases", "Total Deaths", 
                                          "Stringency Index", "Population"])
print(aggregated_data.head())


# In[8]:


data = aggregated_data.sort_values(by=["Total Cases"], ascending=False)
print(data.head())


# In[9]:


data = data.head(10)
print(data)


# In[10]:


data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
                            11497.65, 7027.61, 9946.03, 
                            29564.74, 6001.40, 6424.98, 42354.41]
data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
                            10126.72, 6126.87, 8346.70, 
                            27057.16, 5090.72, 5332.77, 40284.64]
print(data)


# In[11]:


figure = px.bar(data, y='Total Cases', x='Country',
            title="Countries with Highest Covid Cases")
figure.show()


# In[12]:


figure = px.bar(data, y='Total Deaths', x='Country',
            title="Countries with Highest Deaths")
figure.show()


# In[13]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Cases"],
    name='Total Cases',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Deaths"],
    name='Total Deaths',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[14]:


# Percentage of Total Cases and Deaths
cases = data["Total Cases"].sum()
deceased = data["Total Deaths"].sum()

labels = ["Total Cases", "Total Deaths"]
values = [cases, deceased]

fig = px.pie(data, values=values, names=labels, 
             title='Percentage of Total Cases and Deaths', hole=0.5)
fig.show()


# In[15]:


death_rate = (data["Total Deaths"].sum() / data["Total Cases"].sum()) * 100
print("Death Rate = ", death_rate)


# In[16]:


fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='Stringency Index', height=400, 
             title= "Stringency Index during Covid-19")
fig.show()


# In[17]:


fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='GDP Before Covid', height=400, 
             title="GDP Per Capita Before Covid-19")
fig.show()


# In[18]:


fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='GDP During Covid', height=400, 
             title="GDP Per Capita During Covid-19")
fig.show()


# In[19]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["GDP Before Covid"],
    name='GDP Per Capita Before Covid-19',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["GDP During Covid"],
    name='GDP Per Capita During Covid-19',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[20]:


fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='HDI', height=400, 
             title="Human Development Index during Covid-19")
fig.show()


# In[ ]:


"""
the country code
name of all the countries
date of the record
Human development index of all the countries
Daily covid-19 cases
Daily deaths due to covid-19
stringency index of the countries
the population of the countries
GDP per capita of the countries
"""

"""
we studied the spread of covid-19 among the countries and its impact on the global economy.
We saw that the outbreak of covid-19 resulted in the highest number of covid-19 cases and deaths in the united states.
One major reason behind this is the stringency index of the United States. 
It is comparatively low according to the population. We also analyzed how the GDP per capita of every country was affected during the outbreak of covid-19. 
I hope you liked this article on Covid-19 impacts analysis using Python.

"""


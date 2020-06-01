import pandas as pd
import matplotlib.pyplot as plt


#Importing Files
date = 22
df = pd.read_csv (rf'D:\COVID\03-{date}-2020.csv')
density = pd.read_csv (r'D:\COVID\density\pop_density.csv')
#Just for Infected Rate
df = df.drop('Deaths',1)
#Renaming Numbers to reflect Filename Date
df = df.rename(columns={'Deaths': f'03-{date}-2020 Deaths'})
df = df.rename(columns={'Confirmed': f'03-{date}-2020'})

#Trimming Relevant COVID Data for the United States
density = density.drop('2010_POPULATION', 1)

covid = df.loc[df['Country_Region'] == 'US']
covid = covid.drop('FIPS', 1)
covid = covid.drop('Admin2', 1)
covid = covid.drop('Lat', 1)
covid = covid.drop('Long_',1)
covid = covid.drop('Recovered',1)
covid = covid.drop('Active',1)
covid = covid.drop('Country_Region',1)
covid = covid.drop('Last_Update',1)
covid = covid.drop('Combined_Key',1)


#Grouping All Data By State And Totalling Cases/Deaths
covid = covid.groupby('Province_State').sum()

#Merging Both Lists
covid = pd.merge(left=density, right=covid, left_on='STATE_OR_REGION', right_on='Province_State')
covid = covid.drop('2010_DENSITY',1)


#Merging Daily Data Sets
date = 23
col = 0

while date < 32:
    #update = pd.read_csv (rf'D:\COVID\03-{date}-2020.csv', usecols = ['Province_State','Deaths','Confirmed'])
    update = pd.read_csv (rf'D:\COVID\03-{date}-2020.csv', usecols = ['Province_State','Confirmed'])
    #Renaming Numbers to reflect Filename Date
    #update = update.rename(columns={'Deaths': f'03-{date}-2020 Deaths'})
    update = update.rename(columns={'Confirmed': f'03-{date}-2020'})
    update = update.groupby('Province_State').sum()
    covid = pd.merge(left=covid, right=update, left_on='STATE_OR_REGION', right_on='Province_State')
    date += 1
    col +=1 

date=1
while date < 6:
    #update = pd.read_csv (rf'D:\COVID\03-{date}-2020.csv', usecols = ['Province_State','Deaths','Confirmed'])
    update = pd.read_csv (rf'D:\COVID\04-0{date}-2020.csv', usecols = ['Province_State','Confirmed'])
    #Renaming Numbers to reflect Filename Date
    #update = update.rename(columns={'Deaths': f'03-{date}-2020 Deaths'})
    update = update.rename(columns={'Confirmed': f'04-0{date}-2020'})
    update = update.groupby('Province_State').sum()
    covid = pd.merge(left=covid, right=update, left_on='STATE_OR_REGION', right_on='Province_State')
    date += 1
    col +=1 

covid = covid.set_index(['STATE_OR_REGION'])
#Math with Data Values to Add to a new Table For Rate
#df['Val_Diff'] = df['Val10'] - df['Val1']

#covid['av_covid'] = covid.mean(axis=1)
#covid['av_covid'] = covid['av_covid']/col
#print(covid)



# How to select specific Rows and Columns
#set = covid.iloc[1:, 1:]
#labels = covid.iloc[0:,0:1]
#print(labels)
#set.T.plot(figsize=(10,10))

covid.T.plot(figsize=(20,30))
plt.legend(loc='upper left', frameon=False)
#plt.title('COVID Data')
#plt.xlabel('States')
#plt.ylabel('Numbers')

#States with Confirmed Cases and Deaths

#states
#states.plot(figsize=(20,30))
#plt.title('COVID Data')
#plt.xlabel('States')
#plt.ylabel('Numbers')
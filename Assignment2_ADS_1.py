# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def solution(filename,countries,columns,indicator):
    df = pd.read_csv(filename,skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries]
    return df,df.transpose()

filename = 'API_19_DS2_en_csv_v2_4748603.csv'
countries = ['Canada', 'Mexico', 'Belgium', 'North America', 'Chile', 'Kuwait', 'Senegal' ]
columns = ['Country Name', '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
indicators = ['Agricultural land (% of land area)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

cnty_arg_lan,year_arg_lan = solution(filename,countries,columns,indicators[0])
cnty_ele_pro,year_ele_pro = solution(filename,countries,columns,indicators[1])
cnty_for_are,year_for_are = solution(filename,countries,columns,indicators[2])

print(year_arg_lan)


#plotting line graph year on year Trend of the Agricultural land (% of land area) for these 7 countries

plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
plt.plot(year_arg_lan.index,year_arg_lan[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend of the Agricultural land')
plt.xlabel('Year')
plt.ylabel('Agricultural land (% of land area)')
plt.show()

print(year_ele_pro.describe())


#plotting line graph year on year Trend of the Electricity production from coal sources (% of total) for these 7 countries

plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
plt.plot(year_ele_pro.index,year_ele_pro[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend of the Electricity production from coal sources')
plt.xlabel('Year')
plt.ylabel('Electricity production from coal sources (% of total)')
plt.show()

#plotting of grouped bar chart for Electricity production from coal sources (% of total) for different countries over the years

cnty_ele_pro.plot(kind='bar')
plt.title('Electricity production from coal sources')
plt.xlabel('Countries')
plt.ylabel('Electricity production from coal sources')
plt.rcParams["figure.dpi"] = 1500
plt.show()


#plotting of grouped bar chart for Agricultural land (% of land area) for different countries over the years

cnty_arg_lan.plot(kind='bar')
plt.title('Agricultural land')
plt.xlabel('Countries')
plt.ylabel('Forest area (% of land area)')
plt.rcParams["figure.dpi"] = 1500
plt.show()

print(year_arg_lan['Canada'])


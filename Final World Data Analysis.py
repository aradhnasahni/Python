# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:53:20 2018

@author: Kevin

Analysis on World Bank Data specifically for Greater Mediteranian Region
"""

#importing ncessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading world bank files and other files to merge data toegther
proj_file = 'world_data_hult_regions.xlsx'
world_bank=pd.read_excel(proj_file)
pop_file='2014_world_bank_population.xlsx'
pop2014=pd.read_excel(pop_file)
gni_file='2014_GNI.xlsx'
gni2014=pd.read_excel(gni_file)

#filtering for our region and looking at the means
our_region = world_bank[world_bank['Hult_Team_Regions']=='Greater Mediteranian Region']

our_region.mean()
world_bank.mean()

#filtering for columns which have numeric variables
numeric_col=world_bank.iloc[:,5:]
print(numeric_col)
world_bigger=[]
our_region_bigger=[]

#loop to see where our region's average is better or worse compared to the world
for col in numeric_col:
    if world_bank[col].mean() > our_region[col].mean():
        world_bigger.append(col)
    elif world_bank[col].mean() < our_region[col].mean():
        our_region_bigger.append(col)
    else:
        print(f'error for {col}')
print(f"world's average is bigger for {world_bigger}")
print("")
print(f"our regions' average is bigger for {our_region_bigger}")

#adding world bank population file to dataframe
data_with_pop=pd.merge(world_bank,pop2014,on='country_code')
del data_with_pop['country_name_y']

#creating gdp_per_capita column
data_with_pop['gdp_per_capita']=data_with_pop['gdp_usd']/data_with_pop['Population']

#adding world bank GNI file to dataframe   
data_pop_gni=pd.merge(data_with_pop,gni2014,on='country_code')
del data_pop_gni['Country Name']
data_pop_gni['gni_per_capita']=data_pop_gni['GNI 2014']/data_pop_gni['Population']

#filtering income groups similar to our region, high and upper middle incomes
high_income_region = data_pop_gni[data_pop_gni['income_group']=='High income']
upper_middle_inc_region= data_pop_gni[data_pop_gni['income_group']=='Upper middle income']
frames=[high_income_region,upper_middle_inc_region]
high_regs = pd.concat(frames)


#creating excel file with added variables
data_pop_gni.to_excel('world_bank_with_gni2.xlsx')

#imputing values
new_data_median = pd.DataFrame.copy(data_pop_gni)

new_region_median=new_data_median[new_data_median['Hult_Team_Regions']=='Greater Mediteranian Region']

del new_region_median['gdp_usd']
del new_region_median['pct_agriculture_employment']
del new_region_median['incidence_hiv']
del new_region_median['adult_literacy_pct']
del new_region_median['tax_revenue_pct_gdp']

#checking
new_region_median.isnull().any().sum()

#loop to impute values with median for the region
for col in new_region_median:
      if new_region_median[col].isnull().astype(int).sum() > 0:
        col_median = new_region_median[col].median()
        new_region_median[col] = new_region_median[col].fillna(col_median).round(2)

new_region_median.isnull().any().sum()

#imputing hiv and literacy with income group median
new_region_median['incidence_hiv']=new_data_median['incidence_hiv']
new_region_median['adult_literacy_pct']=new_data_median['adult_literacy_pct']

inc_hiv_median=high_regs['incidence_hiv'].median()
inc_lit_median=high_regs['adult_literacy_pct'].median()

new_region_median.isnull().any()

new_region_median['incidence_hiv']= new_region_median['incidence_hiv'].fillna(inc_hiv_median).round(2)
new_region_median['adult_literacy_pct']=new_region_median['adult_literacy_pct'].fillna(inc_lit_median).round(2)

new_region_median.isnull().any()

#manually imputing values for agriculture employment and tax revenue with specific values
new_region_median['pct_agriculture_employment'] = new_data_median['pct_agriculture_employment']
new_region_median['tax_revenue_pct_gdp']= new_data_median['tax_revenue_pct_gdp']

new_region_median.isnull().any()

new_region_median['pct_agriculture_employment'].loc['Gibraltar']=0.2
new_region_median['pct_agriculture_employment'].loc['San Marino']=0.2
new_region_median['tax_revenue_pct_gdp'].loc['Gibraltar']=20.92
new_region_median['tax_revenue_pct_gdp'].loc['San Marino']=40.6
new_region_median['tax_revenue_pct_gdp'].loc['Montenegro']=37.2
new_region_median['tax_revenue_pct_gdp'].loc['Serbia']=42.7

new_region_median.isnull().any()

#Calculating estimated GDP for Gibraltar and imputing


new_region_median['gdp_usd']=new_data_median['gdp_usd']
new_region_median.set_index('country_name_x',inplace=True)
gib_pop=new_region_median.loc['Gibraltar','Population']
print(gib_pop)
gib_gdp=new_region_median['gdp_per_capita'].mean()*gib_pop
print(gib_gdp)


new_region_median['gdp_usd'].loc['Gibraltar']=gib_gdp
print(world_bank['gdp_usd'].median())
print(world_bank['gdp_usd'].median()/gib_pop)

#outlier detection

new_num_cols=new_region_median.iloc[:,5:]

for col in new_num_cols:
    new_num_cols.boxplot(column=[col])
    plt.tight_layout()
    plt.savefig(f'Boxplot for{col} .png')
    plt.show()

region_corr=new_num_cols.corr().round(2)
print(region_corr)

fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(region_corr,cmap='coolwarm',square=True,annot=True,
            linecolor='black',linewidths=0.5)
plt.savefig('imputed heatmap.png')

plt.show()

fig, ax = plt.subplots(figsize=(15,15))
sns.heatmap(region_corr[['gdp_per_capita']],cmap='coolwarm',square=True,annot=True,
            linecolor='black',linewidths=0.5)
plt.savefig('gdp_per_capita_heatmap.png')

plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#############################################################

# Adding some additional data
# 1. Female employment Percentage 
# 2. GeoPolitics Division of the region
# 3. Categorical variable for GeoPolitics
    
added = pd.read_excel('added.xlsx')
reg_impute_add = pd.merge(new_region_median, added, on = 'country_code')

# REGIONS
# Creating seperate datasets for each region (just in case)

Iberia = reg_impute_add[reg_impute_add ['geo_politics'] == 'Iberia']
Balkans = reg_impute_add[reg_impute_add['geo_politics'] == 'Balkans']
Alps = reg_impute_add[reg_impute_add['geo_politics'] == 'Alps']


#Internet usage VS Export by REGION
#Scatter plots!

sns.lmplot(y = 'exports_pct_gdp',
           x = 'internet_usage_pct',
           data = reg_impute_add,
           fit_reg = True,
           hue = 'geo_politics',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Internet Usage VS Export (pct of GDP)\n"+
          "by Region")
plt.grid()
plt.tight_layout()
plt.show()


#Creating GDP column in bln and mln (to simplify)
reg_impute_add['gdp_usd_bln']=(reg_impute_add['gdp_usd']/1000000000).round(2)
reg_impute_add['gdp_usd_mln']=(reg_impute_add['gdp_usd']/1000000).round(2)


# Internet usage and GDP connection 
sns.lmplot(x = 'internet_usage_pct',
           y = 'gdp_usd_bln',
           data = reg_impute_add)

plt.title("Internet Usage VS GDP ($bln)\n"+
          "by Region")
plt.grid()
plt.tight_layout()
plt.show() # OUTLIER - Spain


# What helps with the internet usage? Plotting correlations
# Urban population, compulsory education
sns.pairplot(data = reg_impute_add,
             x_vars = [
                       'urban_population_growth_pct', 
                       'compulsory_edu_yrs'],
             y_vars = ['internet_usage_pct'],
             kind='reg',
             palette = 'plasma')


plt.tight_layout()
plt.savefig('Internet Factors.png')
plt.show()

#####################################
############ MY SOLUTION for normilized axes in the distribution plot for GDP per capita

sns.distplot(reg_impute_add['gdp_per_capita'], kde=True, bins = 'fd',color = 'black',kde_kws={"shade": True},hist=False)
# Plotting hist without kde
ax = sns.distplot(reg_impute_add['gdp_per_capita'], kde=False)
# Creating another Y axis
second_ax = ax.twinx()
#Plotting kde without hist on the second Y axis
sns.distplot(reg_impute_add['gdp_per_capita'], ax=second_ax,kde_kws={"shade": True}, kde=True, hist=False)
#Removing Y ticks from the second axis
second_ax.set_yticks([])

plt.xlabel('GDP per Capita')
plt.show()
########################################################

# Women in parliament VS unemployment_pct (Correlation is not Causation)

sns.lmplot(x = 'women_in_parliament',
           y = 'unemployment_pct',
           data = reg_impute_add,
           fit_reg = True,
           hue = 'geo_politics',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Women in parliament VS GDP\n"+
          "by Region")
plt.grid()
plt.tight_layout()
plt.show()


#########################################################
# HEATMAP - how it all first started
#########################################################

region_corr = reg_impute_add.corr().round(2)

fig, ax = plt.subplots(figsize=(25,25))
sns.heatmap(region_corr,
            cmap = 'Blues',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5)


plt.savefig('Mediterranean region Heatmap.png')
plt.show()



#############################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#############################################################
    

    


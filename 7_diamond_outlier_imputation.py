#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Purpose:
    This code is meant to treat outliers in the diamond dataset
"""



###############################################################################
# Importing libraries and base dataset
###############################################################################
import pandas as pd # data science essentials
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # more data visualization

file ='diamonds_imputed.xlsx'
diamonds = pd.read_excel(file)





###############################################################################
# Outlier detection using quantile techniques
###############################################################################

# Using describe() for distribution analysis 
diamonds.describe()


# We can also use .quantile to set our own parameters for
# distribution analysis
diamonds[['carat',
          'color',
          'clarity',
          'cut',
          'price']].quantile([0.20,
                              0.40,
                              0.60,
                              0.80,
                              1.00])


# See Footnote 1 for an explanation of the code above


###############################################################################
# Outlier detection using boxplots
###############################################################################

# Using boxplots for distribution analysis

"""
Prof. Chase:
    We can use help(pd.DataFrame.boxplot) to find more information on
    the following boxplot() function.
"""

# A basic boxplot
diamonds.boxplot(column = ['carat'])



# A boxplot that's segmented
diamonds.boxplot(column = ['carat'],
                  by = 'channel',)



# A more advanced boxplot that segmented
diamonds.boxplot(column = ['carat'],
                 by = 'channel',
                 vert = False,
                 manage_xticks = False,
                 patch_artist = False,
                 meanline = True,
                 showmeans = True)


plt.title("Carat by Channel")
plt.suptitle("")

plt.show()


# See Footnote 2 for an explanation of the code above



# ...and a more advanced set of boxplots

# carat
diamonds.boxplot(column = ['carat'],
                 by = 'channel',
                 vert = False,
                 patch_artist = True,
                 meanline = True,
                 showmeans = True)



plt.suptitle('')
plt.tight_layout()
plt.savefig('Carat by Channel Boxplot.png')
plt.show()



# color
diamonds.boxplot(column = ['color'],
                 by = 'channel',
                 vert = False,
                 patch_artist = True,
                 meanline = True,
                 showmeans = True)


plt.suptitle('')
plt.tight_layout()
plt.show()



# clarity
diamonds.boxplot(column = ['clarity'],
                 by = 'channel',
                 vert = False,
                 patch_artist = True,
                 meanline = True,
                 showmeans = True)

plt.suptitle('')
plt.tight_layout()
plt.show()



# cut
diamonds.boxplot(column = ['cut'],
                 by = 'channel',
                 vert = False,
                 patch_artist = True,
                 meanline = True,
                 showmeans = True)

plt.suptitle('')
plt.tight_layout()
plt.show()



# carat, color, clarity, and cut
diamonds.boxplot(column = ['carat', 'color', 'clarity', 'cut'],
                 vert = False,
                 manage_xticks = True,
                 patch_artist = False,
                 meanline = True,
                 showmeans = True,
                 )


plt.title("Boxplots for Carat, Color, Clarity, and Cut")

plt.show()



###############################################################################
# Using matplotlib.pyplot
###############################################################################

"""
Prof. Chase:
    Remember, we can use help(plt.boxplot) to find more information on
    'plt.boxplot()'
"""

plt.boxplot(x = 'price',
            data = diamonds,
            vert = False,
            patch_artist = False,
            meanline = True,
            showmeans = True)


plt.xlabel("Price")
plt.show()



###############################################################################
# Refining outlier detection with histograms
###############################################################################

# Using pandas
diamonds['price'].hist()

plt.xlabel("Price")
plt.show()



# Using matplotlib.pyplot
plt.hist(x = 'price',
         data = diamonds)

plt.xlabel("Price")
plt.show()



########################

plt.hist(x = 'price',
         data = diamonds,
         bins = 'fd',
         cumulative = True,
         histtype = 'step'
         )


plt.xlabel("Price")
plt.show()


# See Footnote 3 for an explanation of the code above


########################

plt.hist(x = 'price',
         data = diamonds,
         bins = 'fd',
         cumulative = False,
         histtype = 'barstacked',
         orientation = 'horizontal'
         )


plt.xlabel("Price")
plt.show()



########################
########################

plt.subplot(2, 1, 1)
plt.hist(x = 'price',
         data = diamonds,
         bins = 'fd',
         cumulative = False,
         log = False,
         color = 'black',
         label = 'Log Price'
         )


plt.xlabel("Price")
plt.show()



########################

plt.subplot(2, 1, 2)
plt.hist(x = 'price',
         data = diamonds,
         bins = 'fd',
         cumulative = False,
         log = True,
         color = 'purple',
         label = 'Log Price'
         )


plt.xlabel("Price")
plt.show()



###############################################################################
# Refining graphical displays with seaborn
###############################################################################

# Basic histogram with sns.distplot
sns.distplot(diamonds['price'])

plt.show()


########################

# Customizing with sns.distplot
plt.subplot(2, 2, 1)
sns.distplot(diamonds['price'],
             bins = 10,
             color = 'g')

plt.xlabel('Price')



########################

plt.subplot(2, 2, 2)
sns.distplot(diamonds['carat'],
             bins = 'fd',
             color = 'y')

plt.xlabel('Carat')



########################

plt.subplot(2, 2, 3)
sns.distplot(diamonds['color'],
             bins = 17,
             kde = False,
             rug = True,
             color = 'orange')

plt.xlabel('Color')



########################

plt.subplot(2, 2, 4)

sns.distplot(diamonds['clarity'],
             bins = 17,
             kde = False,
             rug = True,
             color = 'r')


plt.xlabel('Clarity')

plt.tight_layout()
plt.savefig('Diamond Data Histograms 1 of 3.png')

plt.show()



########################
########################

plt.subplot(2, 2, 1)
sns.distplot(diamonds['cut'],
             kde = False,
             rug = True,
             color = 'navy')

plt.xlabel('Cut')



########################

plt.subplot(2, 2, 2)
sns.distplot(diamonds['store'],
             bins = 25,
             kde = False,
             color = 'maroon')

plt.xlabel('Store')



########################

plt.subplot(2, 2, 3)
sns.distplot(diamonds['channel'],
             bins = 8,
             kde = False,
             color = 'gold')

plt.xlabel('Channel')

plt.tight_layout()
plt.savefig('Diamond Data Histograms 2 of 3.png')

plt.show()



###############################################################################
# Outlier cutoff notes (exclusive)
###############################################################################

"""
Prof. Chase:
    By putting our outlier thresholds here, our code is easier to
    maintain. If we would like to adjust our thresholds later, we only
    have to update one part of the code.
"""

price_limit_hi = 12500

carat_limit_0 = 2.03

carat_limit_1 = 1.25

carat_limit_2 = 1.5

color_limit_hi = 7

clarity_limit_lo = 3

clarity_limit_hi = 9



########################
# Histograms with cutoff points
########################

########################

# Customizing with sns.distplot
plt.subplot(2, 2, 1)
sns.distplot(diamonds['price'],
             bins = 35,
             color = 'g')

plt.xlabel('Price')



plt.axvline(x = price_limit_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')


# See Footnote 4 for an explanation of the code above



########################

plt.subplot(2, 2, 2)
sns.distplot(diamonds['carat'],
             bins = 30,
             color = 'y')

plt.xlabel('Carat')



plt.axvline(x = carat_limit_0,
            linestyle = '--',
            color = 'purple')

plt.axvline(x = carat_limit_1,
            linestyle = '--',
            color = 'red')

plt.axvline(x = carat_limit_2,
            linestyle = '--',
            color = 'red')



########################

plt.subplot(2, 2, 3)
sns.distplot(diamonds['color'],
             bins = 17,
             kde = False,
             rug = True,
             color = 'orange')



plt.axvline(x = color_limit_hi,
            linestyle = '--')

plt.xlabel('Color')



########################

plt.subplot(2, 2, 4)

sns.distplot(diamonds['clarity'],
             bins = 17,
             kde = False,
             rug = True,
             color = 'r')

plt.xlabel('Clarity')



plt.axvline(x = clarity_limit_lo,
            linestyle = '--')

plt.axvline(x = clarity_limit_hi,
            linestyle = '--')



plt.tight_layout()
plt.savefig('Diamond Data Histograms 3 of 3.png')



plt.show()



###############################################################################
# Flagging outliers
###############################################################################

diamonds = pd.read_excel(file)


########################
# price
########################

# Writing a variable for outlier flags
diamonds['out_price'] = 0


# Building a for loop
for val in enumerate(diamonds.loc[ : , 'price']):
    
    if val[1] > price_limit_hi:
        diamonds.loc[val[0], 'out_price'] = 1



# Checking to see how many outliers were flagged
diamonds['out_price'].abs().sum()
    

check = (diamonds.loc[ : , ['price', 'out_price']]
                             .sort_values('price',
                                          ascending = False))


# See Footnote 5 for an explanation of the code above



"""
(Advanced)
Prof. Chase:
   Observe the warning in the for loop below. We achieve the same
   result as with the loop above, but at the cost of stability. This
   is why techniques like loc and iloc were invented.
"""

for val in enumerate(diamonds['price']):
    
    if val[1] > price_limit_hi:
        diamonds['out_price'][val[0]] = 1


diamonds['out_price'].abs().sum()



########################
# A more surgical approach to outlier flagging
########################

########################
# carat
########################


diamonds['out_carat'] = 0


for val in enumerate(diamonds.loc[ : , 'carat']):
    
    if diamonds.loc[val[0], 'channel'] == 0 and val[1] > carat_limit_0:
        
        diamonds.loc[val[0], 'out_carat'] = 1



for val in enumerate(diamonds.loc[ : , 'carat']):

    if diamonds.loc[val[0], 'channel'] == 1 and val[1] > carat_limit_1:
        
        diamonds.loc[val[0], 'out_carat'] = 1



for val in enumerate(diamonds.loc[ : , 'carat']):
    
    if diamonds.loc[val[0], 'channel'] == 2 and val[1] > carat_limit_2:
        
        diamonds.loc[val[0], 'out_carat'] = 1


# See Footnote 6 for an explanation of the code above
        
        

diamonds['out_carat'].abs().sum()


check = (diamonds.loc[ : , ['channel', 'carat', 'out_carat']]
                             .sort_values(['channel', 'carat'],
                                          ascending = False))

########################
# clarity
########################

diamonds['out_clarity'] = 0


for val in enumerate(diamonds.loc[ : , 'clarity']):
    
    if val[1] < clarity_limit_lo:
        diamonds.loc[val[0], 'out_clarity'] = 1



for val in enumerate(diamonds.loc[ : , 'clarity']):
    
    if val[1] > clarity_limit_hi:
        diamonds.loc[val[0], 'out_clarity'] = 1



diamonds['out_clarity'].abs().sum()


check = (diamonds.loc[ : , ['clarity', 'out_clarity']]
                             .sort_values(['clarity'],
                                          ascending = False))



########################
# color
########################

diamonds['out_color'] = 0


# Building a for loop
for val in enumerate(diamonds.loc[ : , 'color']):
    
    if val[1] > color_limit_hi:
        diamonds.loc[val[0], 'out_color'] = 1



# Checking to see how many outliers were flagged
diamonds['out_color'].abs().sum()
    

check = (diamonds.loc[ : , ['color', 'out_color']]
                             .sort_values('color',
                                          ascending = False))





########################
# cut
########################

diamonds['out_cut'] = 0



for val in enumerate(diamonds.loc[ : , 'cut']):
    
    if val[1] == 1:
        diamonds.loc[val[0], 'out_cut'] = 1



diamonds['out_cut'].abs().sum()



check = (diamonds.loc[ : , ['cut', 'out_cut']]
                             .sort_values(['cut'],
                                          ascending = False))




########################
# Analyzing outlier flags
########################

diamonds['out_sum'] = (diamonds['out_price']   +
                       diamonds['out_carat']   +
                       diamonds['out_clarity']   +
                       diamonds['out_color'] +
                       diamonds['out_cut'])


# See Footnote 7 for an explanation of the code above



check = (diamonds.loc[ : , ['out_sum',
                            'out_price',
                            'out_carat',
                            'out_clarity',
                            'out_color',
                            'out_cut']].sort_values(['out_sum'],
                                          ascending = False))


# See Footnote 8 for an explanation of the code above



###############################################################################
# Saving things for future use
###############################################################################

diamonds.to_excel('diamonds_flagged.xlsx', index = False)



"""
###############################################################################
# Footnotes
###############################################################################


Footnote 0: the purpose of footnotes

to give a line-by-line explanation of a code snippet


*******************************************************************************


Footnote 1: calling quantiles

diamonds[                                      # calling the diamond dataset
['carat', 'color', 'clarity', 'cut', 'price']  # with columns in a list
].quantile(                                    # calling the quantile function
[0.20, 0.40, 0.60, 0.80, 1.00])                # with specific quantiles in a list


*******************************************************************************


Footnote 2: calling quantiles

diamonds.boxplot(                    # calling boxplot on the diamonds dataset
column = ['carat'],                  # specifying the carat column
by = 'channel',                      # separating the data by the channel column
vert = False,                        # setting vert = False to make horizontal boxplots
manage_xticks = True,                # setting manage_xticks = True to help format the plot
patch_artist = False,                # setting patch_artist = False to get transparent boxes
meanline = True,                     # setting meanline = True to get a line representing the mean
showmeans = True)                    # setting showmeans = True to show the mean and median lines


plt.title("Carat by Channel")        # creating a custom title
plt.suptitle("")                     # supressing the default title

plt.show()                           # displaying the plot


*******************************************************************************


Footnote 3: calling quantiles

plt.hist(                            # calling the histogram function from plt
x = 'price',                         # on the variable price
data = diamonds,                     # from the diamond dataset
bins = 'fd',                         # with the number of bins equal to the Freedman-Diaconis rule
cumulative = True,                   # setting cumulative = True to generate a cumulative distribution
histtype = 'step'                    # setting histtype = 'step' to get steps and a hallow histogram
)                                    # closing the histogram function


plt.xlabel("Price")                  # setting the x-axis label to "Price"
plt.show()                           # displaying the plot



*******************************************************************************


Footnote 4: working with distplot and custom lines

plt.subplot(2, 2,                    # setting a 2 x 2 plot window
1)                                   # and preparing to plot in window 1

sns.distplot(                        # calling distplot from sns
diamonds['price'],                   # on the variable price from the diamonds dataset
bins = 35,                           # specifiying 35 bins
color = 'g')                         # changing the color to green

plt.xlabel('Price')                  # setting the x-axis label to "Price"


plt.axvline(                         # calling a function to create a custom vertical line
x = price_limit_hi,                  # which is drawn at price_limit_hi
label = 'Outlier Thresholds',        # and labeled as 'Outlier Thresholds'
linestyle = '--')                    # and with a '--' line style


*******************************************************************************


Footnote 5: for loop with enumerate

diamonds['out_price'] = 0                    # creating a new column called out_price with all values set to zero


for val in enumerate(                        # starting a for loop where indexes are also called
diamonds.loc[ : , 'price']):                 # on all rows of the column price in the diamonds dataset
    
if val[1] > price_limit_hi:                  # if val[1] (i.e. the value of price) meets this condition
diamonds.loc[val[0], 'out_price'] = 1        # out_price = 1 at the same index (i.e. val[0])


diamonds['out_price']                        # from out_price diamonds
.abs()                                       # take the absolute value of each row
.sum()                                       # and sum the values together
    

check =                                      # creating a variable called check
(diamonds.loc[ : , ['price', 'out_price']]   # that takes all rows of price and out_price from diamonds
.sort_values('price',                        # sorts based on price
ascending = False))                          # and orders so that the highest prices are at the top


*******************************************************************************


Footnote 6: working with distplot and custom lines


diamonds['out_carat'] = 0                    # creating a new variable called out_carat


for val in enumerate(                        # starting a for loop where indexes are also called
diamonds.loc[ : , 'carat']):                 # on all rows of the column price in the diamonds dataset


if diamonds.loc[val[0], 'channel'] == 0      # specifying a condition that subsets observations where channel is equal to zero
and                                          # and also
val[1] > carat_limit_0:                      # that carat is greater than carat_limit_0
        
diamonds.loc[val[0], 'out_carat'] = 1        # and if BOTH of these conditions are true, set out_carat to 1


*******************************************************************************


Footnote 7: creating a new variable: out_sum 


diamonds['out_sum'] =                         # creating a new variable called out_sum
(diamonds['out_price']   +                    # by adding together all of the out_ columns
diamonds['out_carat']   +
diamonds['out_clarity']   +
diamonds['out_color'] +
diamonds['out_cut'])


*******************************************************************************


Footnote 8: checking the content of the outlier flags


check =                                       # creating a variable called check
(diamonds.loc[ : ,                            # from the diamond dataset
['out_sum',                                   # taking all outlier flags including out_sum
'out_price',
'out_carat',
'out_clarity',
'out_color',
'out_cut']
].sort_values(['out_sum'],                    # that is sorted based on out_sum
ascending = False))                           # where the highest value of out_sum is on top

    
*******************************************************************************
"""

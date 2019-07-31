import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def runGDP():
    gdpbycntr = pd.read_csv('GDP.csv')
    print ("Total dataset length: {}",format(len(gdpbycntr)))
    cntrcode = pd.read_csv('CountryCodes.csv')
    gdpDat = gdpbycntr.loc[gdpbycntr['Name'].isin(cntrcode['Name'])]
    print ("Total dataset length: {}",format(len(gdpDat)))
    gdpDat.drop(['CountryCode', 'Indicator', 'Indicator Code'], axis = 1, inplace=True)
    yrs = gdpDat.columns.values[3:]
    countries = ['Congo, Dem. Rep.', 'China']
    datToPlot = gdpDat.loc[gdpDat['Name'].isin(countries)].set_index('Name').T
    datToPlot['Year'] = datToPlot.index.values
    #print (datToPlot.head())
    #datToPlot.to_csv('test.csv')
    buildLinePlot(datToPlot)

def buildLinePlot(dataset):
    palette = sns.color_palette("mako_r", (len(dataset.columns.values)-1))
    dataset = dataset.melt('Year', var_name='Countries',  value_name='GDP')
    ax = sns.lineplot(x='Year', y='GDP',hue='Countries',palette="Paired",  data=dataset)
    plt.show()
if __name__=="__main__":
    runGDP()

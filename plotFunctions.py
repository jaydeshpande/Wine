import matplotlib.pyplot as plt 
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def createScatterPlot(data, countries, yrs, yTitle = None):
    yrLbl = ['1860-69', '70-79', '80-89', '90-99', '1900-09', '10-19', '20-29', '30-39', '40-49',
         '50-59', '60-69', '70-79', '80-89', '90-99', '2000-09', '10-16']
    fig, ax = plt.subplots(figsize=(18, 12))
    for i in countries:
        ax.scatter(yrs, data[data.Country == i][years].values, label = i)
    if yTitle is not None:
        ax.set_ylabel(yTitle, fontsize=16)
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='both', width=2)
    ax.tick_params(which='major', length=10, color='r')
    ax.tick_params(which='minor', length=7, color='k')
    ax.set_xticklabels(yrLbl)
    #ax.tick_params(which='both', length=4, color='r')
    plt.legend()
    plt.show()
    
def createStackedBar(data, countries, yrs, pltTitle = None, yTitle = None, region = None, save=False):
    dtPlt = data[data.Country.isin(countries)].fillna(0).T
    yrLbl = ['1860-69', '70-79', '80-89', '90-99', '1900-09', '10-19', '20-29', '30-39', '40-49',
     '50-59', '60-69', '70-79', '80-89', '90-99', '2000-09', '10-16']
    fig, ax = plt.subplots(figsize=(11, 6))
    if pltTitle is not None:
        ax.set_title(pltTitle)
        
    dtPlt.columns = dtPlt.loc['Country']
    dtPlt.loc[yrs].plot(kind='area', colormap='Spectral', linewidth=0.5, ax=ax, alpha=0.8)
    if yTitle is not None:
        ax.set_ylabel(yTitle)
    ax.set_xlabel('Decades')
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='both', width=2)
    ax.tick_params(which='major', length=10)
    ax.tick_params(which='minor', length=7)
    plt.xlim([1, 15])
    plt.xticks(range(len(yrLbl)), yrLbl)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    plt.show()
    if (save & (region is not None)):
        fig.savefig(region + '_' + pltTitle + '.png', dpi=250, bbox_inches='tight')
    elif (save & (region is None)): 
        fig.savefig(pltTitle + '.png', dpi=250, bbox_inches='tight')
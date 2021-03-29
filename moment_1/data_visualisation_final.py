
from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot

fileName = 'daily-min-temperatures.csv'

def loadFileToDataframe():
    try:
        df = read_csv(fileName, header=0, index_col=0, parse_dates=True, squeeze=True)
        return df
    except IOError:
        print("Something went wrong with reading the file")

def showHeaderInfo(df):
    print(df.head(10))

def showDescribe(df):
    print(df.describe())

def showLinePlot(df):
    df.plot()
    pyplot.show()

def showBoxPlot(df):
    groups = df.groupby(Grouper(freq='A'))
    years = DataFrame()

    for name, group in groups:
	       years[name.year] = group.values

    years.boxplot()
    pyplot.show()

def tryErrorHandling():
    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")

def main():
    df = loadFileToDataframe()
    showHeaderInfo(df)
    showDescribe(df)
    showLinePlot(df)
    showBoxPlot(df)

if __name__ == '__main__':
    main()

import pandas as pd


class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)

    def getDataframe(self):
        return self.df

    def getYearCount(self):
        return self.df.groupby('Year')['Name'].count()

    def getYearSum(self):
        return self.df.groupby('Year')['Name'].sum()

    def getPlatformSum(self):
        return self.df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=True)

    def getRegionData(self, region):
        return self.df[region].sum().sort_values(ascending=True)

    def getRegionAndPlatformData(self, region):
        return self.df.groupby('Platform')[region].sum().sort_values(ascending=True)

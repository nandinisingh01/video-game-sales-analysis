import pandas as pd


class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)

    def getDataframe(self):
        return self.df

    def getYearCount(self):
        return self.df.groupby('Year')['Name'].count()

    def getYearSum(self):
        return self.df.groupby('Year')['Global_Sales'].sum()

    def getPlatformSum(self):
        return self.df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=True)

    def getPlatformCount(self):
        return self.df.groupby('Platform')['Global_Sales'].count().sort_values(ascending=True)

    def getRegionAndPlatformSum(self, region, n):
        return self.df.groupby('Platform').sum().sort_values(region, ascending=False)[region].head(n)

    def getRegionAndPlatformCount(self, region, n):
        return self.df.groupby('Platform').count().sort_values(region, ascending=False)[region].head(n)

    def getRegionAndPublisherSum(self, region, n):
        return self.df.groupby('Publisher').sum().sort_values(region, ascending=False)[region].head(n)

    def getRegionAndPublisherCount(self, region, n):
        return self.df.groupby('Publisher').count().sort_values(region, ascending=False)[region].head(n)

    def getRegionSum(self):
        return self.df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

    def filterPlatform(self, platforms):
        return self.df[self.df['Platform'].isin(platforms)].groupby('Platform').sum()['Global_Sales']

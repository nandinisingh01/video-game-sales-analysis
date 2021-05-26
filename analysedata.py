import pandas as pd



class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path

            def cleanData(self):
        self.df.drop('Rank', inplace=True, axis=1)

    def getPlatformCount(self):




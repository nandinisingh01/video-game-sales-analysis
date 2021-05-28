import pandas as pd

class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)


    def getYearCount(self):
        return self.df.groupby('year')['name'].count()
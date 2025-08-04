import pandas as pd

class DataAnalyzer:
    def __init__(self, df):
        self.df = pd.read_csv(df)

    def total_tweets(self):
        counts = self.df['Biased'].value_counts().to_dict()
        total = len(self.df)
        return {
            "antisemitic": counts.get(1),
            "non_antisemitic": counts.get(0),
            "total": total,
        }

    def average_length(self):
        df = self.df.copy()
        df['Length'] = df['Text'].str.split().apply(len)
        group = df.groupby('Biased')['Length'].mean().to_dict()
        total = df['Length'].mean()
        return {
            "antisemitic": round(group.get(1), 2),
            "non_antisemitic": round(group.get(0), 2),
            "total": round(float(total),2)
        }






da = DataAnalyzer("C:/Users/yakir/PycharmProjects/tweets/data/tweets_dataset.csv")
print(da.total_tweets())
print(da.average_length())

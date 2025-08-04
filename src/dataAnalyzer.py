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

    def longest_3_tweets(self, n = 3):
        df = self.df.copy()
        df['Length'] = df['Text'].apply(len)
        result = {}
        for category in 1, 0:
            tweets = df[df['Biased'] == category].sort_values(by ='Length', ascending=False)['Text'].head(n).tolist()
            result["antisemitic" if category == 1 else "non_antisemitic"] = tweets
        return result

    def common_words(self, n=10):
        df = self.df.copy()
        df['Words'] = df['Text'].str.split()
        words_series = df.explode('Words')['Words']
        top_words = words_series.value_counts().head(n).index.tolist()
        return {f"The 10 most common words in all tweets: {top_words}"}



da = DataAnalyzer("C:/Users/yakir/PycharmProjects/tweets/data/tweets_dataset.csv")
print(da.total_tweets())
print(da.average_length())
print(da.longest_3_tweets())
print(da.common_words())

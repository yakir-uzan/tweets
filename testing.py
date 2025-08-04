def longest_3_tweets(self, n):
    df = self.df.copy()
    df['Length'] = df['Text'].str.split().apply(len)
    result = {}
    for cat in 1, 0:
        tweets = df[df['Biased'] == cat].sort_values(by='Length')['Text'].head(n).tolist()
        result["antisemitic" if cat == 1 else "non_antisemitic"] = tweets
    return result


def common_words(self, n=10):
    df = self.df.copy()
    df['Words'] = df['Text'].str.split()
    words_series = df.explode('Words')['Words']
    top_words = words_series.value_counts().head(n).index.tolist()
    return {"total": top_words}
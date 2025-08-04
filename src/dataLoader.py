import pandas as pd

class DataLoader:
    def load(self, path):
        df = pd.read_csv(path)
        return df
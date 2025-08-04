from src.dataLoader import DataLoader
from src.dataCleaner import DataCleaner

class AppController:
    def __init__(self, data_path):
        self.data_path = data_path
        self.loader = DataLoader()
        self.cleaner = DataCleaner()

    def run(self):
        df = self.loader.load(str(self.data_path))
        df = self.cleaner.clean(df)
import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        # שמירת העמודות הרלוונטיות מתוך קובץ הנתונים
        df = df[['Text', 'Biased']]

        # הסרת סימני פיסוק
        for c in ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '-', '_']:
            df['Text'] = df['Text'].str.replace(c, '')

        #המרה לאותיות קטנות
        df['Text'] = df['Text'].str.lower()

        # הסרת ציוצים ללא סיווג
        df = df[df['Biased'].isin([0, 1])]
        return df

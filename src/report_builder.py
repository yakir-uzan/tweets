import json

class ReportBuilder:
    def __init__(self, df, results_dict):
        self.df = df
        self.results = results_dict

    def export_cleaned_csv(self, path):
        self.df.to_csv(path)

    def export_results_json(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4)

from dataLoader import DataLoader
from dataCleaner import DataCleaner
from dataAnalyzer import DataAnalyzer
from report_builder import ReportBuilder

def main():
    # Loading the data
    loader = DataLoader("C:/Users/yakir/PycharmProjects/tweets/data/tweets_dataset.csv")
    df = loader.load_data()

    # Data cleaning
    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean()

    # Data investigation
    analyzer = DataAnalyzer(cleaned_df)
    results = {
        "total_tweets": analyzer.total_tweets(),
        "average_length": analyzer.average_length(),
        "longest_3_tweets": analyzer.longest_3_tweets(),
        "common_words": analyzer.common_words(),
        }

    # Exporting the output
    report = ReportBuilder(cleaned_df, results)
    report.export_cleaned_csv('../results/tweets_dataset_cleaned.csv')
    report.export_results_json('../results/results.json')

if __name__ == "__main__":
    main()

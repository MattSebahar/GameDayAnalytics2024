import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_csv_to_dict_of_lists(csv_file):
    data_dict = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['text'])
            value = ((str(row['text'])).encode('utf-8'))
            print(value)
            key = row['keyword']
            if key in data_dict:
                print(value)
            else:
                print(value)
                data_dict[key] = [value]
    return data_dict

def text_cleaner(line):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.make
    return line


# Example usage
csv_file_path = 'TestData.csv'
data_association = read_csv_to_dict_of_lists(csv_file_path)
print(data_association)

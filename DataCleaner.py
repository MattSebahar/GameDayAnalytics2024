import csv
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def read_csv_to_dict_of_lists(csv_file):
    data_dict = {}

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            value = ((str(row['text'])).encode('utf-8'))
            key = row['keyword']

            if key in data_dict:
                data_dict[key].append(value)

            else:
                data_dict[key] = [value]

    return data_dict


def sentiment_score(line):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(line)

    return vs


data_association = read_csv_to_dict_of_lists('Vader_data.csv')

keys = []
key_scores = {}

for key in data_association:
    keys.append(key)
    key_scores[key] = 0

    for line in data_association[key]:
        key_scores[key] += sentiment_score(str(line))['compound']


def create_csv1(csv_file_path):
    global key

    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer
        writer = csv.writer(csv_file)

        # Write the header
        writer.writerow(['Brand', 'Score'])

        # Write the dictionary's items
        for key, score in key_scores.items():
            writer.writerow([key, score])


def create_csv2(csv_file_path):
    ss = pd.read_csv('sentiment_scores.csv').filter(items=['Brand'])
    qbr = pd.read_csv('Quarter and Brand Result.csv').filter(items=['brandname'])

    unique_brands = set()

    for brand in qbr['brandname']:
        unique_brands.add(brand)

    for brand in ss['Brand']:
        if brand in unique_brands:
            unique_brands.remove(brand)

    with open('sentiment_scores.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for brand in unique_brands:
            writer.writerow([brand, 0])


# Empty the file
with open('sentiment_scores.csv', 'w') as csv_file:
    pass

# Create the file
create_csv1('sentiment_scores.csv')
create_csv2('sentiment_scores.csv')

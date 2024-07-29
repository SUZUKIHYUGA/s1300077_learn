from collections import Counter
import csv


class frequenciesOfItems:
    def __init__(self, transactionalDatabase, separator=','):
        self.transactionalDatabase = transactionalDatabase
        self.separator = separator
        self.frequencies = self._calculateFrequencies()

    def _calculateFrequencies(self):
        points = []
        with open(self.transactionalDatabase, encoding='UTF-8') as f:
            reader = csv.reader(f, delimiter=self.separator)
            for line in reader:
                for point_str in line:
                    if point_str:
                        for char in ["Point(", ")", "[", "]", "'"]:
                            point_str = point_str.replace(char, "")
                        point_str = point_str.replace(".", "", 1).replace(".", "")
                        longitude, latitude = map(float, point_str.split())
                        points.append((longitude, latitude))
        return dict(Counter(points))

    def getFrequencies(self):
        return self.frequencies

test_csv_file = 'c:/project/s1300077_learn/s1300077_learn/statistics/PM24HeavyPollutionRecordingSensors.csv'

items_frequencies = frequenciesOfItems(test_csv_file)
items_freq_dictionary = items_frequencies.getFrequencies()

for point, count in items_freq_dictionary.items():
    print(f"Point: {point}  Count: {count}")
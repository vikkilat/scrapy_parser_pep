import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.total = len(item['status'])
        self.results[item['status']] = self.results.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now_time = datetime.now().strftime(DATETIME_FORMAT)
        file_name = BASE_DIR / f'results/status_summary_{now_time}.csv'
        total = sum(self.results.values())

        with open(file_name, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.results.items())
            writer.writerow(['Total', total])

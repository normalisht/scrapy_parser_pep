import csv
import datetime as dt
from collections import defaultdict
from os import path

from pep_parse.constants import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(lambda: 0)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.utcnow()
        filename = path.join(
            BASE_DIR, 'results', (
                f'status_summary_{now.strftime("%Y-%m-%d_%H-%M-%S")}.csv'
            )
        )
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect=csv.unix_dialect)
            writer.writerows((
                ('Статус', 'Количество'),
                *self.status_counter.items(),
                ('Всего', sum(self.status_counter.values()))
            ))

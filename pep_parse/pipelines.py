import datetime as dt
from os import path

from pep_parse.constants import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = {}

    def process_item(self, item, spider):
        self.status_counter[item['status']] = (
            self.status_counter.get(item['status'], 0) + 1
        )
        return item

    def close_spider(self, spider):
        now = dt.datetime.utcnow()
        filename = path.join(
            BASE_DIR, 'results', (
                f'status_summary_{now.strftime("%Y-%m-%d_%H-%M-%S")}.csv'
            )
        )
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.status_counter.items():
                f.write(f'{status},{count}\n')
            f.write(f'Всего,{sum(self.status_counter.values())}')

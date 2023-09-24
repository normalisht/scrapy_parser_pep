# scrapy_parser_pep

Этот проект представляет собой готовое решение для скрапинга информации из 
Python Enhancement Proposals (PEP). PEP - это предложения по улучшению Python, 
и этот парсер извлекает информацию о них и сохраняет в два CSV-файла: один с 
информацией о PEP (номер, название, статус), и второй - сводку статусов PEP с 
общим количеством документов.


## Использование
Склонируйте репозиторий на свой локальный компьютер:
```bash
git clone git@github.com:<username>/scrapy_parser_pep.git
```

Перейдите в директорию проекта:
```bash
cd scrapy_parser_pep
```

Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
source venv/Scripts/activate
```

Установите необходимые зависимости
```bash
pip install -r requirements.txt
```

## Работа парсера
После успешного клонирования проекта и перехода в директорию с проектом, 
вы можете выполнить парсинг PEP, следуя этим шагам:

Запустите парсер, выполнив команду:
```bash
scrapy crawl pep
```

Это запустит парсер и начнет собирать информацию о PEP с веб-сайта 
[Python Enhancement Proposals](https://peps.python.org/).

После завершения парсинга, вы найдете два CSV-файла в директории ```results```:

```pep_YYYY-MM-DDTHH-MM-SS.csv```: Этот файл содержит список всех PEP с номерами, 
названиями и статусами. Имя файла будет содержать дату и время выполнения парсинга.

```status_summary_YYYY-MM-DD_HH-MM-SS.csv```: Этот файл содержит сводку статусов PEP 
и общее количество документов PEP. Имя файла также будет содержать дату и время 
выполнения парсинга.

Теперь вы можете анализировать и использовать полученные данные по вашему усмотрению.

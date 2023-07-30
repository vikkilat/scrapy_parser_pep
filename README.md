# Асинхронный парсер PEP

Проект парсера позволяет получать информацию по статусам и количеству PEP.
Полученная информация сохраняется в CSV-файл и содержит номер, название и текущий статус каждого PEP.

## Стек технологий:

* Python 3.7.9
* Scrapy

## Как запустить проект:

* Клонировать репозиторий:

```
git clone git@github.com:vikkilat/scrapy_parser_pep.git
```

* Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:

```
pip install -r requirements.txt
```

* Запустить парсер pep с записью в файл формата csv:
```
scrapy crawl pep
```

## Автор:
[Латышева Виктория](https://github.com/vikkilat)

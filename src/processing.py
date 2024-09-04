def filter_by_state(data, state='EXECUTED'):
    """ Функция, которая фильтрует список словарей по ключу state """
    return [item for item in data if item.get('state') == state]


from datetime import datetime


def sort_by_date(data, descending=True):
    """ Функция, которая список по дате (по умолчанию — по убыванию) """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)


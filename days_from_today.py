from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Convert input string to datetime object. Сalculate days until that date.
    """
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        return (today - date_obj).days
    except ValueError:
        print("Вхідний формат дати невірний!")
        return date


print(get_days_from_today(input("Введіть дату у форматі РРРР-ММ-ДД : ")))

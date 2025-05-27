from datetime import datetime, timedelta
import const

from datetime import datetime

def is_in_current_week(date_str: str) -> bool:
    formats = [
        "%d.%m.%Y %H:%M:%S",
        "%d.%m.%Y %H:%M",
        "%d.%m.%Y"
    ]

    for fmt in formats:
        try:
            record_date = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue
    else:
        raise ValueError(f"Date '{date_str}' is not in a recognized format.")

    # Парсим период из const.dates_period
    start_date_str, end_date_str = const.dates_period.split(',')
    start_of_period = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_of_period = datetime.strptime(end_date_str, "%d-%m-%Y")
    end_of_period = end_of_period.replace(hour=23, minute=59, second=59)

    return start_of_period <= record_date <= end_of_period


def get_last_week_range_func():
    today = datetime.today().date()
    start_date = today - timedelta(days=7)
    return f"{start_date.isoformat()},{today.isoformat()}"
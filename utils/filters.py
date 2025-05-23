from datetime import datetime, timedelta
import const

def is_in_current_week(date_str: str) -> bool:
    date_format = "%d.%m.%Y %H:%M:%S"
    record_date = datetime.strptime(date_str, date_format)
    
    # Парсим период из const.dates_period
    start_date_str, end_date_str = const.dates_period.split(',')
    start_of_period = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_of_period = datetime.strptime(end_date_str, "%d-%m-%Y")
    end_of_period = end_of_period.replace(hour=23, minute=59, second=59)  # Конец дня
    
    return start_of_period <= record_date <= end_of_period

def get_last_week_range_func():
    today = datetime.today().date()
    start_date = today - timedelta(days=7)
    return f"{start_date.isoformat()},{today.isoformat()}"
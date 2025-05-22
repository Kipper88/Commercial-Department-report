from datetime import datetime, timedelta

def is_in_current_week(date_str: str) -> bool:
    date_format = "%d.%m.%Y %H:%M:%S"
    record_date = datetime.strptime(date_str, date_format)

    now = datetime.now()
    now = now.replace(hour=0, minute=0, second=0, microsecond=0)  # для чистоты

    start_of_week = now - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    return start_of_week <= record_date <= end_of_week

def get_last_week_range():
    today = datetime.today().date()
    start_date = today - timedelta(days=7)
    return f"{start_date.isoformat()},{today.isoformat()}"
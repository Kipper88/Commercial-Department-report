from datetime import datetime, timedelta

def is_in_current_week(date_str):
    # Преобразуем строку даты в объект datetime
    date_format = "%d.%m.%Y %H:%M:%S"
    record_date = datetime.strptime(date_str, date_format)

    # Получаем текущую дату и время
    now = datetime.now()

    # Находим понедельник текущей недели
    start_of_week = now - timedelta(days=now.weekday())  # weekday(): 0=Monday, 6=Sunday
    start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

    # Находим конец воскресенья этой недели
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    # Проверяем, находится ли дата в рамках текущей недели
    return start_of_week <= record_date <= end_of_week
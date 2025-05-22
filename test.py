import asyncio
from utils.data.data_form import formatted_data

margin, count_orders, framed_kp, meeting, communications, completed_tasks, plan_activity1, calls_2x_minutes = asyncio.run(formatted_data())

print("🔹 Маржа:", margin)
print("🔹 Кол-во заказов:", count_orders)
print("🔹 Оформленные КП:", framed_kp)
print("🔹 Встречи:", meeting)
print("🔹 Коммуникации:", communications)
print("🔹 Выполненные задачи:", completed_tasks)
print("🔹 План активности:", plan_activity1)
print("🔹 Звонки от 2 минут:", calls_2x_minutes)

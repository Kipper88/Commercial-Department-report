from utils.data.data_form import formatted_data

async def lalala():
    margin,             \
    count_orders,       \
    framed_kp,          \
    meeting,            \
    communications,     \
    completed_tasks,    \
    plan_activity,      \
    calls_2x_minutes = await formatted_data()

import pandas as pd
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/generate-report")
async def generate_excel_report():
    # Создаем DataFrame с данными
    data = {
        "ФИО": [
            "Общий итог", "Антонян Сусанна", "Гаджун Анна", "Косушкина Таисия", 
            "Кочелова Елизавета", "Кулеева Екатерина", "Курочкин Андрей", 
            "Кустов Николай", "Милюкин Федор", "Орлова Ирина", "Панёв Егор", 
            "Панчишкин Андрей", "Танаков Кирилл", "Щеглова Татьяна", 
            "Ключенович Денис", "Трофимова Дарья", "Крузов Евгений"
        ],
        "Маржа": [
            4959736, 390363, 3842816, 135759, "-", 77255, 1, 
            175000, 205858, 7641, "-", 119544, "-", 5500, 
            "-", "-", "-"
        ],
        "Количество заказов": [
            37, 2, 20, 2, "-", 4, 1, 
            2, 1, 1, "-", 3, "-", 1, 
            "-", "-", "-"
        ],
        "Количество оформленных КП": [
            132, 3, 13, 13, 5, 9, 3, 
            7, 19, 21, 0, 1, 14, 13, 
            5, 2, 4
        ],
        "Количество встреч": [
            6, 0, 0, 0, 0, 0, 0, 
            0, 2, 2, 2, 0, 0, 0, 
            0, 0, 0
        ],
        "Количество коммуникаций": [
            168, 0, 0, 20, 3, 3, 8, 
            3, 26, 26, 7, 2, 26, 12, 
            18, 8, 6
        ],
        "Количество выполненых задач": [
            109, 0, 0, 0, 17, 2, 12, 
            1, 11, 8, 0, 0, 43, 3, 
            6, 0, 6
        ],
        "План активности": [
            277, 0, 0, 20, 20, 5, 20, 
            4, 37, 34, 7, 2, 69, 15, 
            24, 8, 12
        ],
        "Звонки от 2х минут": [
            226, 1, 1, 8, 10, 12, 14, 
            46, 14, 3, 17, 5, 27, 7, 
            33, 5, 23
        ]
    }

    df = pd.DataFrame(data)

    # Создаем Excel файл в памяти
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Отчет')
        
        # Получаем workbook и worksheet для дополнительного форматирования
        workbook = writer.book
        worksheet = writer.sheets['Отчет']
        
        # Устанавливаем ширину столбцов
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            worksheet.column_dimensions[column_letter].width = adjusted_width

    output.seek(0)

    # Возвращаем файл как ответ
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=activity_report.xlsx"}
    )
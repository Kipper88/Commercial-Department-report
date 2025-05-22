from utils.data.data_form import formatted_data
import const

import pandas as pd
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

app = FastAPI()

from fastapi import HTTPException
import re
import traceback  # для форматирования стека ошибки

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <form method="post">
        <label>Введите имена и фамилии через запятую:</label><br>
        <textarea name="names" rows="5" cols="50"></textarea><br>
        <button type="submit">Сгенерировать отчет</button>
    </form>
    """

@app.post("/", response_class=StreamingResponse)
async def handle_form(names: str = Form(...)):
    const.workers.clear()
    const.workers.extend([name.strip() for name in names.split(',') if name.strip()])
    const.init_workers_list = {key: 0 for key in const.workers}
    return await generate_excel_report()
        
class NamesRequest(BaseModel):
    names: list[str]
    
async def generate_excel_report():
    try:        
        workers = const.workers
        
        margin, count_orders, framed_kp, meeting, communications, completed_tasks, plan_activity1, calls_2x_minutes = await formatted_data()

        data = {
            "ФИО": ["Общий итог"] + workers,
            "Маржа": [margin[0]] + [margin[1][w] for w in workers],
            "Количество заказов": [count_orders[0]] + [count_orders[1][w] for w in workers],
            "Количество оформленных КП": [framed_kp[0]] + [framed_kp[1][w] for w in workers],
            "Количество встреч": [meeting[0]] + [meeting[1][w] for w in workers],
            "Количество коммуникаций": [communications[0]] + [communications[1][w] for w in workers],
            "Количество выполненых задач": [completed_tasks[0]] + [completed_tasks[1][w] for w in workers],
            "План активности": [plan_activity1[0]] + [plan_activity1[1][w] for w in workers],
            "Звонки от 2х минут": [calls_2x_minutes[0]] + [calls_2x_minutes[1][w] for w in workers],
        }

        df = pd.DataFrame(data)

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Отчет')

            workbook = writer.book
            worksheet = writer.sheets['Отчет']

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

        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=activity_report.xlsx"}
        )
    
    except Exception as e:
        print("❌ Ошибка при генерации отчета:")
        traceback.print_exc()  # выводит стек вызовов
        raise HTTPException(status_code=500, detail=str(e))

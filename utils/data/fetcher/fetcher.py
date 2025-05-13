from ..data_loader import get_resp
from const import init_workers_list, workers
from ...filters import is_in_current_week

async def get_314():
    # МАРЖИНАЛЬНОСТЬ И КОЛ-ВО ЗАКАЗОВ
    data = await get_resp('314', '12042,11749,11752')
    
            
    margin = init_workers_list
    count_orders = init_workers_list 
        
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['11749'] in workers:
                margin[i['11749']] += int(float(i['12042'].replace('.', '').replace(',', '.'))) if i['12042'] != '' else 0
                count_orders[i['11749']] += 1 if i['11752_db_value'] == '6916' else 0
                
    return margin, count_orders
  
# НЕ РАБОТАЕТ ВРЕМЕННО      
async def get_105():
    framed_kp = init_workers_list
    
    return framed_kp
    

async def get_231():
    data_231 = await get_resp('231', '8894,8892')
    
    completed_orders = init_workers_list
    
    for i in data_231:
        people = i['8894']
        if ',' in people:
            # Убираем пробелы до/после запятых
            cleaned = ','.join(part.strip() for part in people.split(','))
            
            # Разбиваем по запятым
            people = [person.strip() for person in cleaned.split(',')]
            people = [p.replace(' ()', '') for p in people]

        if people in workers:
            if is_in_current_week(i['date_added']):
                completed_orders[i['8894']] += 1 if i['8892'] == '6715' else 0
    
    return completed_orders
    
    
# НЕ РАБОТАЕТ ВРЕМЕННО
async def get_152():
    ...
    
async def copleted_orders():
    data = await get_resp('121', '3332,2631,3336')
    data2 = await get_resp('101', '2631,2635')
    
    complete_orders = init_workers_list
    
    for i in data:
        if i['3336'] in workers:
            if is_in_current_week(i['date_added']):
                complete_orders[i['3336']] += 1 if i['3332'] == '4500' else 0
    
    for i in data2:
        if i['2635'] in workers:
            if is_in_current_week(i['date_added']):
                complete_orders[i['2635']] += 1 if i['2631'] == '4500' else 0
                
    return complete_orders
    
async def get_337():
    #data = await get_resp('337', '12009,12010,12011')
    
    calls = init_workers_list
    
    # for i in data:
    #     if is_in_current_week(i['date_added']):
    #         if i['?']:
    #             calls['?'] += 
    
    return calls
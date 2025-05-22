from ..data_loader import get_resp
#from const import const.init_workers_list, const.workers
from ...filters import is_in_current_week

import const

async def get_314():
    # МАРЖИНАЛЬНОСТЬ И КОЛ-ВО ЗАКАЗОВ
    data = await get_resp('314', '11812,11749,11752')
            
    margin = const.init_workers_list.copy()
    count_orders = const.init_workers_list.copy() 
        
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['11749'] in const.workers:
                margin[i['11749']] += int(float(i['11812'].replace('.', '').replace(',', '.'))) if i['11812'] != '' and i['11752_db_value'] == '6916' else 0
                count_orders[i['11749']] += 1 if i['11752_db_value'] == '6916' else 0

    return \
        (sum(i for i in margin.values()), margin),\
        (sum(i for i in count_orders.values()), count_orders)
  
# НЕ РАБОТАЕТ ВРЕМЕННО      
async def get_105():
    data = await get_resp('105', '12571,5628')
    
    framed_kp = const.init_workers_list.copy()
    
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['12571'] in const.workers:
                framed_kp[i['12571']] += 1 if i['5628_db_value'] in ['5487', '5488'] else 0
                
    return (sum(i for i in framed_kp.values()), framed_kp)

async def get_231():
    data_231 = await get_resp('231', '8894,8892')
    
    completed_orders = const.init_workers_list.copy()
    
    for i in data_231:
        people = i['8894']
        if ',' in people:
            # Убираем пробелы до/после запятых
            cleaned = ','.join(part.strip() for part in people.split(','))
            
            # Разбиваем по запятым
            people = [person.strip() for person in cleaned.split(',')]
            people = [p.replace(' ()', '') for p in people]

        for j in people:
            if is_in_current_week(i['date_added']):
                if j in const.workers:
                    completed_orders[j] += 1 if i['8892_db_value'] == '6715' else 0
    
    return (sum(i for i in completed_orders.values()), completed_orders)
    
    
# НЕ РАБОТАЕТ ВРЕМЕННО
async def get_152():
    data = await get_resp('152', '4781')

    result = const.init_workers_list.copy()
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['4781'] in const.workers:
                result[i['4781']] += 1
    
    return (sum(i for i in result.values()), result)
    
    
async def copleted_orders():
    data = await get_resp('121', '3332,2631,3336')
    data2 = await get_resp('101', '2631,2635')
    
    complete_orders = const.init_workers_list.copy()
    
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['3336'] in const.workers:
                complete_orders[i['3336']] += 1 if i['3332_db_value'] == '4500' else 0
    
    for i in data2:
        if is_in_current_week(i['date_added']):
            if i['2635'] in const.workers:
                complete_orders[i['2635']] += 1 if i['2631_db_value'] == '4500' else 0
                
    return (sum(i for i in complete_orders.values()), complete_orders)

async def plan_activity(count_communications, count_completed_tasks):
    result = const.init_workers_list.copy()
    
    for worker in const.workers:
        result[worker] += count_communications.get(worker, 0)
        result[worker] += count_completed_tasks.get(worker, 0)

    total = sum(result.values())
    return total, result
    
async def get_337():
    data = await get_resp('337', '12009,12010,12011,12005')
    
    calls = const.init_workers_list.copy()
    
    rev_workers = {name: ' '.join(reversed(name.split())) for name in const.workers}
    norev_workers = {' '.join(reversed(name.split())): name for name in const.workers}
    
    for i in data:
        if is_in_current_week(i['date_added']):
            if i['12005'] in rev_workers.values():
                calls[norev_workers[i['12005']]] += sum([float(i['12009']), float(i['12010']), float(i['12011'])])
    
    return (sum(i for i in calls.values()), calls)
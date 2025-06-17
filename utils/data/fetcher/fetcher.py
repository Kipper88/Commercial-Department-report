from ..data_loader import get_resp, get_resp_without_filter, get_names_without_comm_departament
from ...filters import is_in_current_week

class CommDepartament():
    def __init__(self, init_workers_list: dict, dates_period: str, workers: list):
        self.init_workers_list = init_workers_list
        self.dates_period = dates_period
        self.workers = workers
        
    async def get_314(self):
        # МАРЖИНАЛЬНОСТЬ И КОЛ-ВО ЗАКАЗОВ
        data = await get_resp('314', '11812,11749,11752', self.dates_period)
                
        margin = self.init_workers_list.copy()
        count_orders = self.init_workers_list.copy() 
            
        for i in data:
            if is_in_current_week(i['date_added'], self.dates_period):
                if i['11749'] in self.workers:
                    margin[i['11749']] += float(i['11812'].replace('.', '').replace(',', '.')) if i['11812'] != '' and i['11752_db_value'] == '6916' else 0
                    count_orders[i['11749']] += 1 if i['11752_db_value'] == '6916' else 0

        return \
            (sum(i for i in margin.values()), margin),\
            (sum(i for i in count_orders.values()), count_orders)
    
    # НЕ РАБОТАЕТ ВРЕМЕННО      
    async def get_105(self):
        data = await get_resp('105', '12571,5628', self.dates_period)
        
        framed_kp = self.init_workers_list.copy()
        
        for i in data:
            if is_in_current_week(i['date_added'], self.dates_period):
                if i['12571'] in self.workers:
                    framed_kp[i['12571']] += 1 if i['5628_db_value'] in ['5487', '5488', '5489'] else 0
                    
        return (sum(i for i in framed_kp.values()), framed_kp)

    async def get_231(self):
        data_231 = await get_resp('231', '8894,8892,8888', self.dates_period)
        
        completed_orders = self.init_workers_list.copy()
        
        for i in data_231:
            people_raw = i['8894']
            # Всегда получаем список имён, даже если одно имя
            people = [p.strip().replace(' ()', '') for p in people_raw.split(',')] if ',' in people_raw else [people_raw.strip().replace(' ()', '')]

            for j in people:
                if is_in_current_week(i['8888'], self.dates_period):
                    if j in self.workers:
                        completed_orders[j] += 1 if i['8892_db_value'] == '6715' else 0
        
        return (sum(completed_orders.values()), completed_orders)
        
        
    # НЕ РАБОТАЕТ ВРЕМЕННО
    async def get_152(self):
        data = await get_resp('152', '4781', self.dates_period)

        result = self.init_workers_list.copy()
        for i in data:
            if is_in_current_week(i['date_added'], self.dates_period):
                if i['4781'] in self.workers:
                    result[i['4781']] += 1
        
        return (sum(i for i in result.values()), result)
        
        
    async def copleted_orders(self):
        data = await get_resp('121', '3332,2631,3336,10571', self.dates_period)
        data2 = await get_resp('101', '2631,2635,7372', self.dates_period)
        
        complete_orders = self.init_workers_list.copy()
        
        for i in data:
            if is_in_current_week(i['10571'], self.dates_period):
                if i['3336'] in self.workers:
                    complete_orders[i['3336']] += 1 if i['3332_db_value'] == '4500' else 0
        
        for i in data2:
            if is_in_current_week(i['7372'], self.dates_period):
                if i['2635'] in self.workers:
                    complete_orders[i['2635']] += 1 if i['2631_db_value'] == '4500' else 0
                    
        return (sum(i for i in complete_orders.values()), complete_orders)

    async def plan_activity(self, count_communications, count_completed_tasks):
        result = self.init_workers_list.copy()
        
        for worker in self.workers:
            result[worker] += count_communications.get(worker, 0)
            result[worker] += count_completed_tasks.get(worker, 0)

        total = sum(result.values())
        return total, result
        
    async def get_337(self):
        data = await get_resp('337', '12009,12010,12011,12005,12006', self.dates_period)
        
        calls = self.init_workers_list.copy()
        
        rev_workers = {name: ' '.join(reversed(name.split())) for name in self.workers}
        norev_workers = {' '.join(reversed(name.split())): name for name in self.workers}
        
        for i in data:
            if is_in_current_week(i['12006'], self.dates_period):
                if i['12005'] in rev_workers.values():
                    calls[norev_workers[i['12005']]] += sum([float(i['12009']), float(i['12010']), float(i['12011'])])
        
        return (sum(i for i in calls.values()), calls)


async def get_68_briefcase(workers, init_workers_list: dict):
    filters = {
        "3676_db_value": {
            "value": "5205", 
            "condition": "search"
        },
        "10062_db_value": {
            "value": "7267", 
            "condition": "search"
        },
        "10062_db_value": {
            "value": "6883", 
            "condition": "search"
        },
        "10062_db_value": {
            "value": "6884", 
            "condition": "search"
        },
        "10062_db_value": {
            "value": "6885", 
            "condition": "search"
        },
    }
    data = await get_resp_without_filter('68', '10062,3617', filters)
    
    workers__ = workers
    
    __actually_first_order = init_workers_list.copy()
    __actually = init_workers_list.copy()
    __re_potencial = init_workers_list.copy()
    __potencial = init_workers_list.copy()

    for i in data:
        if i['3617'] in workers__:
            __actually_first_order[i['3617']] += 1 if i['10062_db_value'] == '7267' else 0
            __actually[i['3617']] += 1 if i['10062_db_value'] == '6883' else 0
            __re_potencial[i['3617']] += 1 if i['10062_db_value'] == '6884' else 0
            __potencial[i['3617']] += 1 if i['10062_db_value'] == '6885' else 0
    
    return \
    (sum(i for i in __actually_first_order.values()), __actually_first_order), \
    (sum(i for i in __actually.values()), __actually), \
    (sum(i for i in __re_potencial.values()), __re_potencial), \
    (sum(i for i in __potencial.values()), __potencial)
from .fetcher.fetcher import *

import asyncio

async def formatted_data(init_workers_list, dates_period, workers):
    # Запускаем все запросы параллельно
    comm_departament = CommDepartament(init_workers_list, dates_period, workers)
    margin_count_orders, framed_kp, meeting, communications, completed_tasks, calls_2x_minutes = await asyncio.gather(
        comm_departament.get_314(),
        comm_departament.get_105(),
        comm_departament.get_231(),
        comm_departament.get_152(),
        comm_departament.copleted_orders(),
        comm_departament.get_337()
    )

    margin, count_orders = margin_count_orders
    
    plan_activity1 = await comm_departament.plan_activity(communications[1], completed_tasks[1])
    
    return margin, count_orders, framed_kp, meeting, communications, completed_tasks, plan_activity1, calls_2x_minutes


async def formatted_data_briefcase(workers, init_workers_list):
    actual_first_order, current, re_potential, potential = await get_68_briefcase(workers, init_workers_list)
    
    return actual_first_order, current, re_potential, potential
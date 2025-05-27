from .fetcher.fetcher import *

import asyncio

async def formatted_data():
    # Запускаем все запросы параллельно
    margin_count_orders, framed_kp, meeting, communications, completed_tasks, calls_2x_minutes = await asyncio.gather(
        get_314(),
        get_105(),
        get_231(),
        get_152(),
        copleted_orders(),
        get_337()
    )

    margin, count_orders = margin_count_orders
    
    plan_activity1 = await plan_activity(communications[1], completed_tasks[1])
    
    return margin, count_orders, framed_kp, meeting, communications, completed_tasks, plan_activity1, calls_2x_minutes


async def formatted_data_briefcase():
    actual_first_order, current, re_potential, potential = await get_68_briefcase()
    
    return actual_first_order, current, re_potential, potential

from fetcher.fetcher import *

async def formatted_data():
    # готово
    margin, count_orders = await get_314()
    
    # не пашет
    #framed_kp = await get_105()
    
    # готово
    meeting = await get_231()
    
    # не пашет
    #communications = await get_152()
    
    
    completed_tasks = await copleted_orders()
    
    
    plan_activity = ...
    
    calls_2x_minutes = ...
    
    return margin, count_orders, framed_kp, meeting, communications, completed_tasks, plan_activity, calls_2x_minutes
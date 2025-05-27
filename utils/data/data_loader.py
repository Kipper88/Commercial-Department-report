from const import *
from aiohttp import ClientSession, ClientTimeout
import const

async def get_resp(entity_id, select_fields):
    params = {
            'key': apiKeyRuk,
            'username': usernameRuk,
            'password': passRuk,
            'action': 'select',
            'entity_id': entity_id,
            'select_fields': select_fields,
          #  'limit': 500,
            'filters': {
                'date_added': const.dates_period
            }
    }
    
    async with ClientSession() as sess:
        resp = await sess.get(
            url=urlRuk,
            json=params,
            ssl=False
        )
        data = await resp.json(content_type='text/html')
        data = data['data']
        
        return data
    
async def get_names():
    data = await get_resp('104', '2439,2438,10768,7470')
    
    names = []
    
    for i in data:
        names.append(f"{i['2439']} {i['2438']}") if i['10768_db_value'] == '6987' and i['7470_db_value'] in ['6753', '6754', '6392'] else ...
    
    return names

async def get_resp_without_filter(entity_id, select_fields):
    params = {
            'key': apiKeyRuk,
            'username': usernameRuk,
            'password': passRuk,
            'action': 'select',
            'entity_id': entity_id,
            'select_fields': select_fields,
    }
    
    timeout = ClientTimeout(total=3600, sock_connect=3600, sock_read=3600)
    async with ClientSession(timeout=timeout) as sess:
        resp = await sess.get(
            url=urlRuk,
            json=params,
            ssl=False
        )
        data = await resp.json(content_type='text/html')
        data = data['data']
        
        return data
from const import *
from aiohttp import ClientSession
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
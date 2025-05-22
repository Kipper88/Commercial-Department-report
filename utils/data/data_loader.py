from const import *
from aiohttp import ClientSession
from ..filters import get_last_week_range

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
                'date_added': get_last_week_range()
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
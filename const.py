from dotenv import dotenv_values

__vars = dotenv_values('.env')

apiKeyRuk = __vars.get('apiKeyRuk', '')
urlRuk = 'https://btg-sped.ru/crm/api/rest.php'
usernameRuk = __vars.get('usernameRuk', '')
passRuk = __vars.get('passRuk', '')


workers = [
]

init_workers_list = {}
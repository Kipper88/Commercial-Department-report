from dotenv import dotenv_values

__vars = dotenv_values('.env')

apiKeyRuk = __vars.get('apiKeyRuk', '')
urlRuk = 'https://btg-sped.ru/crm/api/rest.php'
usernameRuk = __vars.get('usernameRuk', '')
passRuk = __vars.get('passRuk', '')


workers = [
    "Сусанна Антонян",
    "Анна Гаджун",
    "Таисия Косушкина",
    "Елизавета Кочелова",
    "Екатерина Кулеева",
    "Андрей Курочкин",
    "Николай Кустов",
    "Федор Милюкин",
    "Ирина Орлова",
    "Егор Панёв",
    "Андрей Панчишкин",
    "Кирилл Танаков",
    "Татьяна Щеглова",
    "Денис Ключенович",
    "Дарья Трофимова",
    "Евгений Крузов"
]

init_workers_list = {key: 0 for key in workers}
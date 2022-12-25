from config.cur_abbrevations import cur_abbrevations

available_currencies = ''
for currency in cur_abbrevations.keys():
    available_currencies += f'* {currency}\n'

values_command_message = f'''Доступные валюты:

{available_currencies}
'''

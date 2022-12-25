import requests
from classes import APIException
from config import cur_abbrevations


class Converter:
    """Класс используемый для запроса и конвератации валюты."""

    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> str:
        """Совершает запрос для конвертации валюты.

        base - наименование валюты, цену которой пользователь хочет узнать.
        quote - наименование валюты, в которую требуется совершить перевод.
        amount - сумма валюты.
        """

        base_abbr = cur_abbrevations[base]
        quote_abbr = cur_abbrevations[quote]
        url = f'https://min-api.cryptocompare.com/data/price?fsym={base_abbr}&tsyms={quote_abbr}'
        timeout = 5

        try:
            # можно воспользоваться встроенной библиотекой json,
            # но requests может самостоятельно декодировать ответ
            response = requests.get(url, timeout=timeout).json()
        except requests.HTTPError:
            raise APIException('Сервер не ответил, попробуйте позже.')
        except requests.Timeout:
            raise APIException(f'Сервер не ответил в течении {timeout} секунд. Операция прервана.')
        except requests.JSONDecodeError:
            raise APIException('Не удалось обработать ответ сервера, попробуйте позже.')

        if quote_abbr in response:
            cur_rate = response[quote_abbr]
            total_amount = "{:.2f}".format(cur_rate * float(amount))
            return f'Стоимость: {total_amount} {quote_abbr}'
        else:
            raise APIException('Не удалось получить стоимость уазанной валюты, попробуйте позже.')


if __name__ == '__main__':
    base = 'доллар'
    quote = 'рубль'
    amount = '1'

    result = Converter.get_price(base, quote, amount)
    print(result)

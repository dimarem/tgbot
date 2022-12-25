from classes import APIException
from config import cur_abbrevations


class RequestParser:
    """Данный класс отвечает за разбор пользовательского запроса."""

    @staticmethod
    def parse_request(request: str) -> tuple:
        """Разбирает пользовательский запрос. В качестве результата возвращает кортеж, первым элементом которого
        является наименование валюты, цену которой пользователь хочет узнать; вторым - наименование валюты, в которую
        требуется совершить перевод; третьим - сумма валюты.

        Если разбор был неудачным выбрасывает исключение типа APIException.
        """

        parts = request.split(' ')

        if len(parts) != 3:
            raise APIException(
                'Запрос должен содержать три указателя, воспользуйтесь командой "/start", чтобы узнать подробности.')

        if parts[0] not in cur_abbrevations or parts[1] not in cur_abbrevations:
            raise APIException(
                'Недопустимые наименования валют, воспользуйтесь командой "/values", чтобы узнать подробности.')

        try:
            cur_sum = float(parts[2])
        except Exception:
            raise APIException(
                'Недопустимое значение суммы, воспользуйтесь командой "/start", чтобы узнать подробности.')

        if cur_sum < 0:
            raise APIException(
                'Сумма должна быть больше ноля, воспользуйтесь командой "/start", чтобы узнать подробности.')

        return parts[0], parts[1], parts[2]


if __name__ == '__main__':
    invalid_request_1 = "a"
    invalid_request_2 = "a b"
    invalid_request_3 = "a b c d"
    invalid_request_4 = "a b c"
    invalid_request_5 = "рубль доллар 123abc345"
    invalid_request_6 = "рубль доллар 0"
    invalid_request_7 = "рубль доллар -1"
    valid_request = "рубль доллар 1"

    try:
        RequestParser.parse_request(invalid_request_1)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_2)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_3)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_4)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_5)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_6)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(invalid_request_7)
    except APIException as e:
        print(e)

    try:
        RequestParser.parse_request(valid_request)
        print("Correct")
    except APIException as e:
        print(e)

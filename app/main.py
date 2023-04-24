import datetime

from app.utils import load_json_sorted


def create_mask(string):
    """
    Маскирует строчное выражение с номером счета или карты
    :param string: строка, полученная из json-файла
    :return: замаскированная строка с номерами реквезитов
    """
    if "Счет" in string:
        unmasked_string = string[:-20]
        masked_string = (2 * '*' + string[-4:])[-6:]
        return unmasked_string + masked_string
    elif len(string) == 0:
        return ""
    else:
        unmasked_string = string[0:-16]
        masked_string = (
                string[-16:-12] + " " + string[-12:-10]
                + 2 * '*' + ' ' + 4 * '*' + ' ' + string[-4:])
        return unmasked_string + masked_string


def print_transactions():
    """
    Выводит последние 5 транзакций из файла json
    """
    data = load_json_sorted()[:5]
    result = []
    for item in data:
        date = datetime.datetime.strptime(item["date"], '%Y-%m-%dT%H:%M:%S.%f').date()
        formatted_date = datetime.datetime.strftime(date, '%d.%m.%Y')

        description = item["description"]

        try:
            from_ = item["from"]
        except KeyError:
            from_ = ""
        masked_from_ = create_mask(from_)

        to_ = item["to"]
        masked_to = create_mask(to_)

        amount = item["operationAmount"]["amount"]

        currency = item["operationAmount"]["currency"]["name"]

        result_string = f"{formatted_date} {description}\n" \
                 f"{masked_from_} -> {masked_to}\n" \
                 f"{amount} {currency}\n"
        result.append(result_string)
    return result
print(type(print_transactions()[0]))

if __name__ == "__main__":
    data_to_print = print_transactions()
    for item in data_to_print:
        print(item)

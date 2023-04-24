import json
import operator
import os.path
import datetime


def load_json_sorted():
    """
    Загружает данные из json-файла,фильтрует пустые словари,
    сортирует словари по убыванию даты, фильтрует транзакции по значению "EXECUTED"
    :return: отсортированный по убыванию даты список словарей с данными
    """
    filedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(filedir[:-3], "operations.json"), "r", encoding="UTF-8") as file:
        data = json.load(file)
        filtered_data = filter(None, data)
        sorted_data = sorted(filtered_data, key=operator.itemgetter('date'), reverse=True)
        executed_transactions = [d for d in sorted_data if d["state"] == "EXECUTED"]
        return executed_transactions


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
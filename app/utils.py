import json
import operator
import os.path


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


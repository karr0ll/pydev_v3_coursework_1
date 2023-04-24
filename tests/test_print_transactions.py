from app.main import print_transactions


def test_print_transactions():
    assert isinstance(print_transactions(), list) is True
    assert print_transactions()[0] == "08.12.2019 Открытие вклада\n -> Счет **5907\n41096.24 USD\n"


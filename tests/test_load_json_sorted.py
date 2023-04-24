from main.utils import load_json_sorted

def test_load_json_sorted():
    assert load_json_sorted()[1] == {
        'id': 114832369,
        'state': 'EXECUTED',
        'date': '2019-12-07T06:17:14.634890',
        'operationAmount': {
            'amount': '48150.39',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }
        },
        'description': 'Перевод организации',
        'from': 'Visa Classic 2842878893689012',
        'to': 'Счет 35158586384610753655'
    }
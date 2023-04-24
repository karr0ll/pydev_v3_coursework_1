import os

from app.main import create_mask

def test_create_mask():
    assert create_mask('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert create_mask('Счет 64686473678894779589') == 'Счет **9589'
    assert create_mask('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'
    assert create_mask('') == ''




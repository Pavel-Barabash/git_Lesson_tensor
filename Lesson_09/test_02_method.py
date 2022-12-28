import job_02 as md


def test_sum_6_2():
    """Тест на сложение."""
    assert md.sum_dig(6, 2) == 8
    assert md.sum_dig(6, 2) != 4


def test_dif_6_2():
    """Тест на вычитание."""
    assert md.dif_dig(6, 2) == 4
    assert md.dif_dig(6, 2) != 15


def test_multi_6_2():
    """Тест на умножение."""
    assert md.multi_dig(6, 2) == 12
    assert md.multi_dig(6, 2) != 20


def test_divis_dig_6_2():
    """Тест на деление."""
    assert md.divis_dig(6, 2) == 3
    assert md.divis_dig(6, 2) != 1


def test_expo_dig_6_2():
    """Тест на возведение в степень."""
    assert md.expo_dig(6, 2) == 36
    assert md.expo_dig(6, 2) != 30


def test_div_modul_6_2():
    """Тест на деление по модулю."""
    assert md.div_modul_dig(6, 2) == 0
    assert md.div_modul_dig(6, 2) != 9


def test_int_div_6_2():
    """Тест на целочисленные деления."""
    assert md.int_div_dig(6, 2) == 3
    assert md.int_div_dig(6, 2) != 11


def test_decimal_4_and_1_dot_3():
    """Тест операции с дробным числом"""
    assert md.sum_dig(4, 1.3) == 5.3

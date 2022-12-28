import job_01 as md


def test_pass_len_5():
    """Проверка пароля по минимальной длине 6 символов."""
    assert md.password('Frgh2') == False


def test_pass_not_all_int():
    """Не должен состоять только из цифр."""
    assert md.password('6234523467') == False


def test_pass_not_password_name():
    """Проверка на содержание password в пароле."""
    assert md.password('password') == False


def test_pass_good():
    """Пароль проходит по всем параметрам."""
    assert md.password('GoodPas2022') == True

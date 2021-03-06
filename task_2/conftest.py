import pytest


@pytest.fixture
def init_data():
    return {
        "name": "Билли Херингтон",
        "phone": "555-0100",
        "birthday": "14.07.1969",
        "address": "США, Нью-Йорк, 48th Ave, дом 4, кв.27"
    }


@pytest.fixture
def init_data_message():
    return (
        "Билли Херингтон — адрес: США, Нью-Йорк, 48th Ave, дом 4, кв.27,"
        " телефон: 555-0100, день рождения: 14.07.1969"
    )


@pytest.fixture
def vlad_message():
    return (
        "Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3,"
        " кв. 12, телефон: 73-88, день рождения: 19.07.1893"
    )


@pytest.fixture
def mike_message():
    return (
        "Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская,"
        " дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891"
    )

try:
    import precode
except ModuleNotFoundError:
    assert False, "Работа не найдена"

import importlib


def test_precode_print_contact():
    if hasattr(precode, "print_contact"):
        assert False, "Переименуйте функцию print_contact и перенесите её в класс Contact"


def test_init(init_data):
    assert hasattr(precode, "Contact"), "Не найден класс Contact"
    data = precode.Contact(**init_data)
    attrs = ("name", "phone", "birthday", "address",)

    for attr in attrs:
        assert hasattr(data, attr), f"Проверьте наличие атрибута {attr}"
        assert data.__dict__[attr] == init_data.get(attr)


def test_show_contact(init_data, init_data_message, capsys):
    data = precode.Contact(**init_data)
    # чтобы не ловить ниже сообщение "Создаем ноый контакт", а ловить только метод .show_contact()
    _, _ = capsys.readouterr()
    assert hasattr(data, 'show_contact'), "Проверьте наличие метода show_contact в классе Contact"
    assert hasattr(data.show_contact, '__call__'), "Проверьте наличие метода show_contact в классе Contact"

    data.show_contact()
    output_message, _ = capsys.readouterr()
    assert init_data_message == output_message.strip("\n"), "Проверьте выводимое сообщение в методе show_contact"


def test_instances(vlad_message, mike_message, capsys):
    assert hasattr(precode, "vlad"), "Проверьте, что объект vlad создан"
    assert isinstance(precode.vlad, precode.Contact), "Объект vlad должен быть экземпляром класса Contact"
    precode.vlad.show_contact()
    vlad_output_message, _ = capsys.readouterr()
    assert vlad_message == vlad_output_message.strip("\n"), "Проверьте сообщение которое выводит метод show_contact для объекта vlad"

    assert hasattr(precode, "mike"), "Проверьте, что объект mike создан"
    assert isinstance(precode.mike, precode.Contact), "Объект mike должен быть экземпляром класса Contact"
    precode.mike.show_contact()
    mike_output_message, _ = capsys.readouterr()
    assert mike_message == mike_output_message.strip("\n"), "Проверьте сообщение которое выводит метод show_contact для объекта mike"


def test_user_output(capsys):
    # авторский вывод работы
    with open('output.txt', 'r') as file:
        author_output = file.read()
    # reload модуля для того чтобы отловить все принты, так как не обернуто в if __name__ == '__main__'
    # (так же можно запускать код через subprocess)
    importlib.reload(precode)
    user_output_message, _ = capsys.readouterr()
    assert author_output == user_output_message, "Проверьте выводимое сообщение метода show_contact"







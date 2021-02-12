import re

import author
from usercode import usercode

try:
    import precode
except (TypeError, IndentationError):
    assert False, "Допишите функцию cache_args"


def get_code(match_line, usercode):
    """Функция возвращает заданный участов кода."""
    result = []
    match = False
    indentation = None
    for line in usercode.split('\n'):
        check_indentation = len(line) - len(line.strip())
        if re.search(match_line, line):
            match = True
            result.append(line)
            indentation = len(line) - len(line.strip())
            continue
        elif indentation == check_indentation and not line.strip().startswith('#'):
            break
        elif match:
            result.append(line)
    return '\n'.join(result)


def test_time_imported():
    assert hasattr(author, 'time'), "Импортируйте модуль time"


def test_functions_exists():
    functions = ("time_check", "cache_args", "long_heavy")
    for func in functions:
        assert hasattr(precode, func), f"Проверьте наличие функции {func}. Не удаляйте её."


def test_cache_args_dict():
    result = get_code("def cache_args", usercode)
    search_str = r'\s*=\s*{}|\s*=\s*dict\(\)'
    assert re.search(search_str, result), "Проверьте наличие словаря в функции cache_args"


def test_cache_return_from_dict():
    search_str = r"\s*return\s*\w+\[\w+\]|\s*return\s*\w+\.get\(\w+\)"
    assert re.search(search_str, usercode), "Проверьте,  что возвращаетет закешированное значение"


def test_long_heavy_func(capsys):
    mesage_before = "Время выполнения функции: 1.0 с."
    author_func = author.long_heavy(5)
    author_output, _ = capsys.readouterr()

    user_func = precode.long_heavy(5)
    user_output, _ = capsys.readouterr()

    assert author_func == user_func, "Функция long_heavy возвращает неверное значение"
    assert author_output.strip() == mesage_before
    assert user_output.strip() == mesage_before

    cached_msg = "Время выполнения функции: 0.0 с."
    author.long_heavy(5)
    cached_author_output, _ = capsys.readouterr()

    precode.long_heavy(5)
    cached_user_output, _ = capsys.readouterr()

    assert cached_author_output.strip() == cached_msg
    assert cached_user_output.strip() == cached_msg

    # сравниваем зекешированное значение, с незакешированным
    author.long_heavy(3)
    uncached_author_output, _ = capsys.readouterr()
    precode.long_heavy(5)
    cached_precode_output, _ = capsys.readouterr()

    assert uncached_author_output != cached_precode_output








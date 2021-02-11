import re

import author

try:
    import precode
except (TypeError, IndentationError):
    assert False, "Допишите функцию make_divider_of"

from usercode import usercode


def get_code(match_line, usercode):
    """Функция возвращает заданный участок кода."""
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


def test_devider_exists():
    assert hasattr(precode, "make_divider_of"), "Проверьте наличие функции make_divider_of"


def test_division_operation_exist():
    # забираем участок кода
    result = get_code('def division_operation', usercode)
    assert result, "Не изменяйте название функции division_operation"


def test_division_operation_return():
    # проверяем что make_divider_of возвращает не значение, а другую функцию
    user_code_block = get_code('def make_divider_of', usercode)
    search_str = r"\s*return\s*divisible\s*\/\s*divider"
    assert re.search(search_str, user_code_block), "Проверьте, что функция make_divider_of возвращает division_operation"


def test_div2():
    assert hasattr(precode, "div2"), "Проверьте наличие переменной div2 И не меняйте её имя"
    assert hasattr(precode.div2, "__call__"), "Убедитесь, что тип перменной div2 - function"

    precode_div2_result = precode.div2(10)
    author_div2_result = author.div2(10)
    assert author_div2_result == precode_div2_result, "div2 возвращает неправильное значение"


def test_div5():
    assert hasattr(precode, "div5"), "Проверьте наличие переменной div5 и не меняйте её имя"
    assert hasattr(precode.div5, "__call__"), "Убедитесь, что тип перменной div5 - function"

    precode_div5_result = precode.div2(20)
    author_div5_result = author.div2(20)
    assert author_div5_result == precode_div5_result, "div5 возвращает неправильное значение"


def test_make_divider_of_function():
    result = precode.div2(precode.div5(20))
    assert result == 2, "Функция make_divider_of возвращает неправильное значение"


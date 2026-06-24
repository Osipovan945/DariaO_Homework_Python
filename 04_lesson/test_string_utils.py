import pytest
from string_utils import StringUtils

utils = StringUtils()

# 1. ТЕСТЫ ДЛЯ МЕТОДА CAPITALIZE


@pytest.mark.parametrize("input_string, expected_result", [
    # Позитивные тесты
    pytest.param("skypro", "Skypro", id="обычное_слово"),
    pytest.param("hello world", "Hello world", id="фраза_с_пробелом"),
    pytest.param("python", "Python", id="слово_с_маленькой_буквы"),
    pytest.param("123abc", "123abc", id="начинается_с_цифры"),
    pytest.param("a", "A", id="один_символ"),
    pytest.param("", "", id="пустая_строка"),
    pytest.param(" ", " ", id="только_пробел"),
    pytest.param("SKYPRO", "Skypro", id="уже_заглавные_буквы"),
])
def test_capitalize(input_string, expected_result):
    assert utils.capitalize(input_string) == expected_result

# 2. ТЕСТЫ ДЛЯ МЕТОДА TRIM (удаление пробелов в начале)


@pytest.mark.parametrize("input_string, expected_result", [
    # Позитивные тесты
    pytest.param("   skypro", "skypro", id="пробелы_в_начале"),
    pytest.param("skypro", "skypro", id="без_пробелов"),
    pytest.param("   hello world", "hello world",
                 id="пробелы_в_начале_с_пробелом_внутри"),
    pytest.param("   ", "", id="только_пробелы"),
    pytest.param("", "", id="пустая_строка"),
    pytest.param("\t skypro", "\t skypro", id="табуляция_в_начале"),
    pytest.param("   a", "a", id="один_символ_с_пробелами"),
    pytest.param("  123", "123", id="цифры_с_пробелами"),
])
def test_trim(input_string, expected_result):
    assert utils.trim(input_string) == expected_result

# 3. ТЕСТЫ ДЛЯ МЕТОДА CONTAINS (проверка наличия символа)


@pytest.mark.parametrize("input_string, symbol,expected_result", [
    # Позитивные тесты (символ найден)
    pytest.param("SkyPro", "S", True, id="символ_в_начале"),
    pytest.param("SkyPro", "o", True, id="символ_в_конце"),
    pytest.param("SkyPro", "y", True, id="символ_в_середине"),
    pytest.param("123", "2", True, id="цифра_найдена"),
    pytest.param("hello", "l", True, id="повторяющийся_символ"),

    # Негативные тесты (символ не найден)
    pytest.param("SkyPro", "U", False, id="символа_нет_1"),
    pytest.param("SkyPro", "z", False, id="символа_нет_2"),
    pytest.param("", "a", False, id="пустая_строка_символа_нет"),
    pytest.param(" ", "a", False, id="только_пробел_символа_нет"),
    pytest.param("abc", "d", False, id="символа_нет_в_строке"),
    pytest.param("123", "4", False, id="цифры_нет"),

    # Граничные случаи
    pytest.param("a", "a", True, id="один_символ_совпадает"),
    pytest.param("a", "b", False, id="один_символ_не_совпадает"),
])
def test_contains(input_string, symbol, expected_result):
    assert utils.contains(input_string, symbol) == expected_result

# 4. ТЕСТЫ ДЛЯ МЕТОДА DELETE_SYMBOL (удаление символа)


@pytest.mark.parametrize("input_string, symbol, expected_result", [
    # Позитивные тесты (символ удаляется)
    pytest.param("SkyPro", "k", "SyPro", id="удаление_одного_символа"),
    pytest.param("SkyPro", "Pro", "Sky", id="удаление_подстроки"),
    pytest.param("hello", "l", "heo", id="удаление_повторяющегося_символа"),
    pytest.param("123", "2", "13", id="удаление_цифры"),
    pytest.param("a b c", " ", "abc", id="удаление_пробела"),
    pytest.param("test", "t", "es", id="удаление_символа_в_начале_и_конце"),

    # Негативные тесты (символ не найден)
    pytest.param("SkyPro", "z", "SkyPro", id="символа_нет_строка_не_меняется"),
    pytest.param("hello", "x", "hello", id="другой_символ_не_найден"),
    pytest.param("", "a", "", id="пустая_строка_удаление"),
    pytest.param(" ", "a", " ", id="только_пробел_символ_не_найден"),

    # Граничные случаи
    pytest.param("a", "a", "", id="удаление_единственного_символа"),
    pytest.param("aaa", "a", "", id="удаление_всех_символов"),
    pytest.param("abc", "", "abc", id="пустой_символ_для_удаления"),

    # Сложные сценарии
    pytest.param("Hello World", "l", "Heo Word", id="удаление_буквы_из_фразы"),
    pytest.param("Python Programming", "m", "Python Prograing",
                 id="удаление_буквы_из_длинного_слова"),
    pytest.param("123-456-789", "-", "123456789", id="удаление_разделителя"),
    pytest.param("   spaces   ", " ", "spaces", id="удаление_всех_пробелов"),
])
def test_delete_symbol(input_string, symbol, expected_result):
    assert utils.delete_symbol(input_string, symbol) == expected_result

# ============================================
# 8. ТЕСТЫ ДЛЯ ОБНАРУЖЕНИЯ БАГОВ
# ============================================

# @pytest.mark.parametrize("input_string, expected", [
#     # Проверка на баг в trim - он удаляет пробелы ТОЛЬКО в начале
#     ("  hello  ", "hello  "),    # Ожидаем: пробелы в конце остаются
#     ("   world   ", "world   "), # Ожидаем: пробелы в конце остаются

#     # Проверка на баг в contains - неправильная обработка
#     ("SkyPro", "S", True),       # работает правильно
#     ("SkyPro", "P", True),       # работает правильно
# ])
# def test_bug_scenarios(input_string, expected):
#     """
#     Тесты, которые могут выявить баги в реализации
#     """
#     assert utils.trim(input_string) == expected

# ============================================
# 10. ПАРАМЕТРИЗАЦИЯ С ID ДЛЯ ЛУЧШЕЙ ВИДИМОСТИ
# ============================================


@pytest.mark.parametrize("input_string, expected", [
    pytest.param("test", "Test", id="простое_слово"),
    pytest.param("hello world", "Hello world", id="с_пробелом"),
    pytest.param("", "", id="пустая_строка"),
    pytest.param(" ", " ", id="только_пробел"),
    pytest.param("123", "123", id="только_цифры"),
])
def test_capitalize_with_ids(input_string, expected):
    """
    Тест с явными ID для каждого случая
    При запуске pytest будет показывать эти ID
    """
    assert utils.capitalize(input_string) == expected

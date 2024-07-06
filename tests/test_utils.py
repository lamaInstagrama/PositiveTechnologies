import pytest
from utils import full_equal_dict, part_equal_dict


@pytest.mark.parametrize('d1, d2', [
    # Пустые словари
    (
            {}, {}
    ),

    # "Пустые" значения
    (
            {'xYz': '', 'AbC': 0, 'c': {}, '': ''},
            {'xyz': '', 'ABC': 0, 'C': {}, '': ''}
    ),

    # Нет вложенности, ключи в разном порядке
    (
            {'a': 1, 'c': 'how ARE you?', 'b': 'Hello!'},
            {'A': 1, 'B': 'HELLO!', 'C': 'HoW ArE yOu?'}
    ),

    # Есть вложенность
    (
            {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}, 'g': 5},
            {'A': 1, 'b': {'C': 2, 'd': {'E': 3, 'F': 4}}, 'G': 5}
    ),
    # Сложная вложенность
    (
            {
                "very_long_key_1": {
                    "another_very_long_key_1": {
                        "deeply_nested_key_1": "some_string_value_1",
                        "deeply_nested_key_2": 123,
                        "deeply_nested_key_3": "another_string_value_1",
                    },
                    "another_very_long_key_2": {
                        "deeply_nested_key_4": 456,
                        "deeply_nested_key_5": "yet_another_string_value_1",
                    },
                },
                "very_long_key_2": {
                    "another_very_long_key_3": {
                        "deeply_nested_key_6": 789,
                        "deeply_nested_key_7": "final_string_value_1",
                    },
                },
            },
            {
                "VERY_LONG_KEY_1": {
                    "ANOTHER_very_LONG_KEY_1": {
                        "deeply_NEsted_key_1": "SOME_string_vaLue_1",
                        "deeply_nesTed_keY_2": 123,
                        "deeply_neSted_key_3": "anotheR_strinG_value_1",
                    },
                    "ANOTHER_VERY_LONG_KEY_2": {
                        "deepLY_nested_kEy_4": 456,
                        "deeply_nested_key_5": "yEt_another_string_value_1",
                    },
                },
                "VERY_LONG_KEY_2": {
                    "anoTHer_very_long_key_3": {
                        "deeply_nested_kEy_6": 789,
                        "deeply_nested_key_7": "finaL_string_value_1",
                    },
                },
            }

    )

])
def test_full_equal_dict_positive(d1: dict, d2: dict):
    assert full_equal_dict(d1, d2) is True


@pytest.mark.parametrize('d1, d2', [
    # Разное количество ключей
    (
            {},
            {'a': 1}
    ),
    (
            {'abc': '12d'},
            {}
    ),
    (
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you?'},
            {'a': 1, 'C': 'HoW ArE yOu?'}
    ),

    # Разные ключи
    (
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you?'},
            {'a': 1, 'b': 'Hello!', 'd': 'how ARE you?'}
    ),

    # Разные значения
    (
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you?'},
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you'}
    ),

    # Разные ключи для вложенных словарей
    (
            {'a': 1, 'b': 'Hello!', 'c': {'': ''}},
            {'a': 1, 'b': 'Hello!', 'c': {'1': ''}}
    ),

    # Разное количество ключей для вложенных словарей
    (
            {'a': 1, 'b': 'Hello!', 'c': {'': ''}},
            {'a': 1, 'b': 'Hello!', 'c': {'': '', '1': 1}}
    ),

    # Разные значения во вложенных словарях
    (
            {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 5}}, 'g': 5},
            {'A': 1, 'b': {'C': 2, 'd': {'E': 3, 'F': 4}}, 'G': 5}
    ),
    (
            {
                "very_long_key_1": {
                    "another_very_long_key_1": {
                        "deeply_nested_key_1": "some_string_value_1",
                        "deeply_nested_key_2": 123,
                        "deeply_nested_key_3": "another_string_value_1",
                    },
                    "another_very_long_key_2": {
                        "deeply_nested_key_4": 456,
                        "deeply_nested_key_5": "yet_another_string_value_1",
                    },
                },
                "very_long_key_2": {
                    "another_very_long_key_3": {
                        "deeply_nested_key_6": 789,
                        "deeply_nested_key_7": "final_string_value_1",
                    },
                },
            },
            {
                "VERY_LONG_KEY_1": {
                    "ANOTHER_very_LONG_KEY_1": {
                        "deeply_NEsted_key_1": "SOME_string_vaLue_1",
                        "deeply_nesTed_keY_2": 123,
                        "deeply_neSted_key_3": "anotheR_strinG_value_1",
                    },
                    "ANOTHER_VERY_LONG_KEY_2": {
                        "deepLY_nested_kEy_4": 456,
                        "deeply_nested_key_5": "yEt_another_string_value_1",
                    },
                },
                "VERY_LONG_KEY_2": {
                    "anoTHer_very_long_key_3": {
                        "deeply_nested_kEy_6": 789,
                        "deeply_nested_key_7": "finaL_string_value_2",
                    },
                },
            }
    )

])
def test_full_equal_dict_negative(d1: dict, d2: dict):
    assert full_equal_dict(d1, d2) is False


@pytest.mark.parametrize('d1, d2', [
    # Пустые словари
    (
            {}, {}
    ),
    # Пустые значения
    (
            {'a': 0, 'b': '', '': {}},
            {'a': 0, 'b': '', '': {}},
    ),

    # Второй словарь пустой
    (
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you?'},
            {}
    ),

    # Разное количество ключей
    (
            {'a': 1, 'b': 'Hello!', 'c': 'how ARE you?'},
            {'a': 1, 'C': 'how ARE you?'}
    ),

    # Разное количество ключей во вложенных словарях
    (
            {'a': 1, 'b': {'c': 2, 'd': 3, 'e': 4}, 'g': 5, 'dr': {'Helo', 'World'}},
            {'a': 1, 'b': {'c': 2, 'd': 3}, 'DR': {}}
    ),
    (
            {
                'a': 1,
                'b': 'hello',
                'c': {
                    'd': 2,
                    'e': 'world',
                    'f': {'g': 3, 'h': 'test'}
                },
                'i': '1, 2, 3',
                'j': {'k': 4, 'l': 'another test', 'm': {'n': 5, 'o': 'final test'}}
            },
            {
                'A': 1,
                'C': {
                    'd': 2,
                    'f': {'h': 'TeSt'}
                },
                'j': {'l': 'ANOTHER TEST', 'm': {'n': 5}}
            }
    )

])
def test_part_equal_dict_positive(d1: dict, d2: dict):
    assert part_equal_dict(d1, d2) is True


@pytest.mark.parametrize('d1, d2', [
    # Разные ключи
    (
            {'1': '1', '2': '2'},
            {'2': '1', '3': '2'}
    ),

    # Разные значения
    (
            {'1': 1, '2': '2', 'hello': 'world'},
            {'1': 1, '2': '2', 'hello': 'world!'}
    ),

    # Разные ключи во вложенных словарях
    (
            {'1': 1, '2': '2', 'world': {'1': 2}},
            {'1': 1, '2': '2', 'world': {'2', 1}}
    ),
    # Разные значения во вложенных словарях
    (
            {'1': 1, '2': '2', 'world': {'1': 'AbC'}},
            {'1': 1, '2': '2', 'world': {'2', 'cAb'}}
    ),

    # Второй словарь больше
    (
            {}, {'': ''}
    ),
    (
            {'1': '1', '2': '2', 'AbC': {'1': '2'}},
            {'1': '1', '2': '2', 'AbC': {'1': '2', 'AbC': {'1': '2'}}},
    ),
    (
            {
                'a': 1,
                'b': 'hello',
                'c': {
                    'd': 2,
                    'e': 'world',
                    'f': {'g': 3, 'h': 'test'}
                },
                'i': [1, 2, 3],
                'j': {'k': 4, 'l': 'another test', 'm': {'n': 5, 'o': 'final test'}}
            },
            {
                'A': 1,
                'B': 'Hello',
                'C': {
                    'd': 2,
                    'e': 'World',
                    'f': {'g': 3, 'h': 'TeSt'}
                },
                'j': {'k': 4, 'l': 'ANOTHER TEST', 'm': {'n': 5, 'o': 'Final Test', 'ExtraKey': 'ExtraValue'}},
            }

    ),

])
def test_part_equal_dict_negative(d1: dict, d2: dict):
    assert part_equal_dict(d1, d2) is False

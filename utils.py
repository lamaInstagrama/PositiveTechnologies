def full_equal_dict(dict_1: dict, dict_2: dict) -> bool:
    """
     Проверяет на равенство два словаря. Dict считаются равными, если:
         - на всех уровнях вложенности все элементы совпадают;
         - ни один из словарей не содержит лишних ключей;
         - при этом строки и ключи считаются равными, если они равны в нижнем регистре (i.e. ASD считается равным AsD);

     Dict может содержать:
         - строки;
         - числа (int);
         - вложенные словари (dict) с такими же ограничениями;

    Возвращает True, если словари равны, иначе False
    """
    dict_1 = {k.lower(): v for k, v in dict_1.items()}
    dict_2 = {k.lower(): v for k, v in dict_2.items()}

    # Равенство ключей
    if dict_1.keys() != dict_2.keys():
        return False

    # Равенство значений
    for k, v1 in dict_1.items():
        v2 = dict_2[k]

        if isinstance(v1, int):
            if v1 != v2:
                return False

        elif isinstance(v1, str):
            if isinstance(v2, str):
                if v1.lower() != v2.lower():
                    return False
            else:
                return False

        elif isinstance(v1, dict):
            if isinstance(v2, dict):
                res = full_equal_dict(v1, v2)
                if not res:
                    return False
            else:
                return False

    return True


def part_equal_dict(dict_1: dict, dict_2: dict) -> bool:
    """
    Проверяет на равенство два словаря. Dict считаются равными, если:
        - словарь 1 может содержать больше ключей, чем словарь 2;
        - на всех уровнях вложенности все элементы совпадают;
        - при этом строки и ключи считаются равными, если они равны в нижнем регистре (i.e. ASD считается равным AsD);

    Dict может содержать:
        - строки;
        - числа (int);
        - вложенные словари (dict) с такими же ограничениями

    Возвращает True, если словари равны, иначе False
    """
    dict_1 = {k.lower(): v for k, v in dict_1.items()}
    dict_2 = {k.lower(): v for k, v in dict_2.items()}

    # dict_1 может быть больше, чем dict_2.
    # Проверка, что все ключи из dict_2 есть в dict_1
    if not all(k in dict_1 for k in dict_2):
        return False

    # Равенство значений.
    # Т.к. dict_1 >= dict_2, то итерироваться надо по dict_2
    for k, v2 in dict_2.items():
        v1 = dict_1[k]

        if isinstance(v1, int):
            if v1 != v2:
                return False

        elif isinstance(v1, str):
            if isinstance(v2, str):
                if v1.lower() != v2.lower():
                    return False
            else:
                return False

        elif isinstance(v1, dict):
            if isinstance(v2, dict):
                # res = full_equal_dict(v1, v2)  # Если требуется полное совпадение вложенных словарей
                res = part_equal_dict(v1, v2)  # Если условиями задачи допустимо, что v1 >= v2
                if not res:
                    return False
            else:
                return False

    return True

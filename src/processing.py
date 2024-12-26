from typing import List, Dict

dictionary_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

def filter_by_state(dictionary_list: list[dict[str]], state: str = "EXECUTED") -> List[Dict]:
    """Функция сортировки данных по параметру "EXECUTED" в списке словарей"""
    return [every_dict for every_dict in dictionary_list if every_dict.get("state") == state]


def sort_by_date(dictionary_list: list[dict[str]], reverse_list: bool = True) -> list[dict[str]]:
    """Функция принимает список и сортирует его по датам по убыванию"""

    sorted_list = sorted(dictionary_list,key=lambda every_dict: every_dict["date"], reverse = reverse_list)

    return sorted_list

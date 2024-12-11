from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_info: str) -> str:
    """Функция маскирующая номер карты, или счета"""
    if "Счет" in user_info:
        return f"Счет {get_mask_account(user_info)}"

    else:
        number_card = get_mask_card_number(user_info[-16:])
        return user_info.replace(user_info[-16:],number_card)


def get_date(user_date: str) -> str:
    """Функция возвращающая дату в формате "дд.мм.гггг" """ #"2024-03-11T02:26:18.671407"
    return user_date[8:10] + "." + user_date[5:7] + "." + user_date[0:4]

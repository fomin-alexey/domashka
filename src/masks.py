def get_mask_card_number(card_number: str) -> str:
    """Функция которая маскирует номер карты, заменяя часть цифр на *"""
    return card_number[0:4] + " " + card_number[5:7] + "** **** " + card_number[-4:]


def get_mask_account(account: str) -> str:
    """Функция которая маскирует номер счета, заменяя часть цифр на *"""
    return "**" + account[-4:]


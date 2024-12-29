import pytest
from src.masks import get_mask_card_number


def test_card_number():
    assert get_mask_card_number('1596837868705199') == "1596 83** **** 5199"
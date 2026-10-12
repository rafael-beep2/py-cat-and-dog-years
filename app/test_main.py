
from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_cat_age_boundaries() -> None:
    assert get_human_age(14, 0)[0] == 0
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(23, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(31, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_age_boundaries() -> None:
    assert get_human_age(0, 14)[1] == 0
    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 23)[1] == 1
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 33)[1] == 3
    assert get_human_age(0, 34)[1] == 4

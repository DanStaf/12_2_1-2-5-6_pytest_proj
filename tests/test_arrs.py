import pytest
from utils import arrs



def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


@pytest.fixture
def input_array():
    return [1,2,3]

@pytest.fixture
def blank_array():
    return []


def test_slice(input_array, blank_array):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(input_array, 1) == [2, 3]

    assert arrs.my_slice(blank_array, 1) == blank_array
    assert arrs.my_slice(input_array) == input_array
    assert arrs.my_slice(input_array, end=2) == [1, 2]


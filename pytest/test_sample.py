import csv
import os
from typing import List

from sample import (
    add_two_int,
    load_csv_num_and_sort,
    quantize_symmetric,
    quantize_symmetric_bugged,
)

import pytest


# simple case
def test_add_two_int():
    assert add_two_int(1, 2) == 3
    assert add_two_int(4, -1) == 3
    assert add_two_int(-1, -1) == -2
    # assert add_two_int(2, 0) == 3 # fail
    assert add_two_int(100, 1) == 101


# parameterized test
@pytest.mark.parametrize(
    ("real_val", "scale", "expected"),
    [(2.0, 0.008, 250), (1.4, 0.0001, 255), (1.0, 0.01, 100)],
)
def test_quantize_symmetric(real_val, scale, expected):
    assert quantize_symmetric(real_val, scale) == expected


@pytest.mark.parametrize(
    ("real_val", "scale", "expected"),
    [(2.0, 0.008, 250), (1.4, 0.0001, 255), (1.0, 0.01, 100)],
)
def test_quantize_symmetric_bugged(real_val, scale, expected):
    assert quantize_symmetric_bugged(real_val, scale) == expected


# fixture
@pytest.fixture
def csv_fixture() -> str:
    # preprocessing
    csv_path = "numbers.csv"
    num_list = [2, -1, 0, 15]
    with open(csv_path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(num_list)

    yield csv_path

    # postprocessing
    os.remove(csv_path)


def test_load_csv_num_and_sort(csv_fixture):
    assert load_csv_num_and_sort(csv_fixture) == [-1, 0, 2, 15]

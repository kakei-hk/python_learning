import math
from typing import List

import numpy as np


def add_two_int(int_a: int, int_b: int) -> int:
    return int_a + int_b


def quantize_symmetric(real_val: float, scale: float) -> int:
    """
    This function symmetrically quantizes input real value (float)
    with the specified scale (float value).
    Only 8bit is supported.

    real_val = scale * quant_val

    """
    assert scale >= 0.0, "Invalid scale! Scale value must be positive."

    quant_min = 0
    quant_max = 255

    quant_val = real_val / scale
    quant_val_clip = np.clip(math.floor(quant_val), quant_min, quant_max)

    return quant_val_clip


def quantize_symmetric_bugged(real_val: float, scale: float) -> int:
    """
    This function symmetrically quantizes input real value (float)
    with the specified scale (float value).
    Only 8bit is supported.

    real_val = scale * quant_val

    """
    assert scale >= 0.0, "Invalid scale! Scale value must be positive."

    quant_min = 0
    quant_max = 255

    quant_val = real_val / scale
    # quant_val_clip = np.clip(math.floor(quant_val), quant_min, quant_max)
    # quantized value must be clipped as above
    quant_val_clip = math.floor(quant_val)

    return quant_val_clip


def load_csv_num_and_sort(csv: str) -> List[int]:
    """
    This function loads a csv file with some numbers as follows.
    Only int type is supported.
    2,-1,40,5
    Then return the numbers as a sorted list in ascending order as follows.
    [-1, 2, 5, 40]
    """
    with open(csv) as f:
        num_list = sorted(map(lambda n: int(n), f))

    return num_list

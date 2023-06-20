"""
File: rich-example.py
Author: Chuncheng Zhang
Date: 2023-06-20
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Example for rich module
    rich: https://github.com/Textualize/rich

    $ pip install rich

    It shows how to merge the rich into your code.
    And the inspect function gives you a full list of the attributes.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-06-20 ------------------------
# Requirements and constants
from enum import Enum
import pandas as pd

from rich import print, inspect

# %% ---- 2023-06-20 ------------------------
# Function and class

# %% ---- 2023-06-20 ------------------------
# Play ground
# Print the pandas DataFrame,
# it consists in both IPython and console.
iris = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris)

# %% ---- 2023-06-20 ------------------------
# Pending
# Print all the attributes.
inspect(['foo', 'bar'], all=True)

# Print all but the value, in case the value is too long.
inspect(iris, all=True, value=False)

# %% ---- 2023-06-20 ------------------------
# Pending


class Color(Enum):
    RED = 1
    BLUE = 2


color = Color
inspect(color)


# %%

# %%

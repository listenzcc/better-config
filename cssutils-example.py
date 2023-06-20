"""
File: omega.py
Author: Chuncheng Zhang
Date: 2023-06-20
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Example of cssutils module.

    cssutils: https://pypi.org/project/cssutils/

    $ pip install cssutils

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-06-20 ------------------------
# Requirements and constants
import cssutils

from rich import print, inspect


# %% ---- 2023-06-20 ------------------------
# Function and class
# Example CSS string
css_string = """
body {
    font-family: Arial, sans-serif;
    font-size: 14px;
    color: #333;
}

h1, h2, h3 {
    font-weight: bold;
    color: #000;
}

.container {
    width: 960px;
    margin: 0 auto;
}
"""

# Converting CSS to YAML

sheet = cssutils.parseString(css_string)
print(sheet)
inspect(sheet, all=True, value=False)


# %% ---- 2023-06-20 ------------------------
# Play ground

# %%

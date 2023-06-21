"""
File: defines.py
Author: Chuncheng Zhang
Date: 2023-06-20
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-06-20 ------------------------
# Requirements and constants
import sys
import logging
import matplotlib as mpl

from enum import Enum
from pathlib import Path
from omegaconf import OmegaConf
from dataclasses import dataclass

from rich import print, inspect


# %% ---- 2023-06-20 ------------------------
# Function and class

class Mode(Enum):
    unknown = -1000
    notReady = -100
    loadConfig = -9
    checkFolder = -8
    loadAsset = -7
    display = -6
    waitStart = -5
    idle = 0
    busy = 1
    RSVP = 2
    SSVEP = 3
    MI = 4


class LoggingLevel(Enum):
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    FATAL = logging.FATAL
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL


@dataclass
class LocalServer:
    local: str = '0.0.0.0'
    port: int = 7788
    coding: str = 'utf-8'
    chroot: Path = Path('D:\\')
    mode: Mode = Mode.unknown
    loggingLevel: LoggingLevel = LoggingLevel.DEBUG


@dataclass
class Display:
    display: int = 0
    width: int = 1440
    height: int = 900
    font: Path = Path('C:\\windows\\fonts\\harlowsi.ttf')


@dataclass
class RSVP:
    # Display
    displayX: int = 200
    displayY: int = 100
    borderWidth: int = 2
    borderColor: str = 'cyan'
    backgroundColor: str = 'gray'
    backgroundImage: str = 'RSVP/background.png'

    # Whether to resize the image to the display
    resizeFlag: bool = True
    width: int = 800
    height: int = 600

    # Experiment design
    imagesPerSecond: int = 10
    targetImageFolder: str = 'RSVP/images/target-images'
    otherImageFolder: str = 'RSVP/images/other-images'
    specialImageFolder: str = 'RSVP/images/special-images'

    # Setup for random sequence
    randomSequenceFlag: bool = True
    chunkRepeats: int = -1  # -1 refers to infinite
    chunkLength: int = 100
    targetsEachChunk: int = 3
    minGapBetweenTargets: int = 10
    headSpecialImages: int = 10
    tailSpecialImages: int = 10


# %% ---- 2023-06-20 ------------------------
# Play ground


oc = OmegaConf.create(dict(
    rsvp=RSVP,
    display=Display,
    local_server=LocalServer,
    # css4_colors=mpl.colors.CSS4_COLORS
))

with open('oc.yaml', 'w') as f:
    f.write(OmegaConf.to_yaml(oc, sort_keys=True))

print('\nDefault:\n', oc)


# %% ---- 2023-06-20 ------------------------
# Pending
# Merge with cli input
cli_oc = OmegaConf.from_cli(sys.argv[1:])
print('\nCli:\n', cli_oc)

merged_oc = OmegaConf.merge(oc, cli_oc)
print('\nMerged:\n', merged_oc)
print()

# %% ---- 2023-06-20 ------------------------
# Pending

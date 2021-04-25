#NOTES START
"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""

"""
This command is a dataclass that encapsulates a bookmark
This uses type hints: https://docs.python.org/3/library/typing.html
"""
#NOTES END
import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddDailyLogCommand(Command):
    id: int
    IDMeal: int
    MealName: str
    calories: int
    protein: int
    adddate : str
    editdate: str

@dataclass
class UpdateDailyLogCommand(Command):
    id: int
    IDMeal: int
    MealName: str
    calories: int
    protein: int
    adddate : str
    editdate: str


@dataclass
class ListDailyLogCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteDailyLogCommand(Command):
    id: int


@dataclass
class AddExerciseLogCommand(Command):
    id: int
    Name: str
    xfactor: int
    duration: int
    caloriesburned: int
    adddate : str
    editdate: str

@dataclass
class UpdateExerciseLogCommand(Command):
    id: int
    Name: str
    xfactor: int
    duration: int
    caloriesburned: int
    adddate : str
    editdate: str


@dataclass
class LisExerciseLogCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteExerciseLogCommand(Command):
    id: int
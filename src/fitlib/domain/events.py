from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import DailyLog, ExerciseLog



class Event(ABC):
    pass


@dataclass
class DailyLogAdded(Event):
    id: int
    IDMeal: int
    MealName: str
    calories: int
    protein: int
    adddate : str
    editdate: str

@dataclass
class DailyLogUpdated(Event):
    id: int
    IDMeal: int
    MealName: str
    calories: int
    protein: int
    adddate : str
    editdate: str

@dataclass
class DailyLogListed(Event):
    DailyLog: list[DailyLog]

@dataclass
class DailyLogDeleted(Event):
    DailyLog: DailyLog
    



@dataclass
class ExerciseLogAdded(Event):
    id: int
    Name: str
    xfactor: int
    duration: int
    caloriesburned: int
    adddate : str
    editdate: str

@dataclass
class ExerciseLogUpdated(Event):
    id: int
    Name: str
    xfactor: int
    duration: int
    caloriesburned: int
    adddate : str
    editdate: str

@dataclass
class ExerciseLogListed(Event):
    ExerciseLog: list[ExerciseLog]

@dataclass
class ExerciseLogDeleted(Event):
    ExerciseLog: ExerciseLog


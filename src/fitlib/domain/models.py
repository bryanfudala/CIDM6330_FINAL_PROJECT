from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional

"""
Pure domain bookmark:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""

class Bio:

    def __init__(self, id: int, user: str, weight: str, bmr: str, adddate: datetime, editdate: datetime):
        self.id : int = id
        self.title : str = user
        self.weight : int = weight
        self.bmr : int = bmr
        self.adddate : str = adddate
        self.editdate : str = editdate
        self.events = []

class DailyLog:

    def __init__(self, id: int, IDMeal: str, mealname: str, calories: int, protein: int, adddate: datetime, editdate: datetime):
        self.id : int = id
        self.IDMeal : str = IDMeal
        self.mealname : str = mealname
        self.calories : int = calories
        self.protein : int = protein
        self.adddate : str = adddate
        self.editdate : str = editdate
        self.events = []

class ExcerciseLog:

    def __init__(self, id: int, name: str, xfactor: int, duration: int, caloriesburned: int, adddate: datetime, editdate: datetime):
        self.id : int = id
        self.name : str = name
        self.xfactor : int = xfactor
        self.duration : int = duration
        self.caloriesburned : int = caloriesburned
        self.adddate : str = adddate
        self.editdate : str = editdate
        self.events = []

class Meals:
    def __init__(self, id: int, name: str, protein: int, carbs: int, fats: int, calories: int, adddate: datetime, editdate: datetime):
        self.id : int = id
        self.name : str = name
        self.protein : int = protein
        self.carbs : int = carbs
        self.fats : int = fats
        self.calories : int = calories
        self.adddate : str = adddate
        self.editdate : str = editdate
        self.events = []

class Exercise:
    def __init__(self, id: int, name: str, xfactor: int, adddate: datetime, editdate: datetime):
        self.id : int = id
        self.name : str = name
        self.xfactor : int = xfactor
        self.adddate : str = adddate
        self.editdate : str = editdate
        self.events = []
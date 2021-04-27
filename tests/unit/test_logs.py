from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from fitlib.domain import commands, models
from fitlib.services import handlers, unit_of_work
from fitlib.adapters import repository

from fitlib.adapters.orm import start_mappers











def test_adding_record_to_dailylog(session):
    x = models.DailyLog(1, 20, "spinachrolls", 100,10)

    x_repository = repository.SqlAlchemyRepository(session)
    x_repository.add(x)
    session.commit()

    rows = session.execute(
        'SELECT ID , IDMeal, MealName, calories, protein FROM "dailylog"'
    )
    assert list(rows) == [(1, 20, "spinachrolls", 100,10)]


def test_computation_of_calories(session):
    x = models.Meals(1, "protein bar", 20, 20, 9, 250)

    x_repository = repository.SqlAlchemyRepository(session)
    x_repository.add(x)
    session.commit()
    
    y = session.execute(
        'SELECT Calories  FROM "Meals" WHERE ID=1'
    )

    assert y == 250

def test_biometrics_update(session):
    x = models.Bio(190)

    x_repository = repository.SqlAlchemyRepository(session)
    x_repository.edit(x)
    session.commit()
    
    y = session.execute(
        'SET WEIGHT = 190  FROM "Meals" WHERE ID=1'
    )

    assert y == 190

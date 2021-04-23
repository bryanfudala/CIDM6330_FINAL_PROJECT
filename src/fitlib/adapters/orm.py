import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)
from sqlalchemy.log import InstanceLogger

from sqlalchemy.orm import registry, mapper, relationship

from fitlib.domain.models import Bio, DailyLog, ExcerciseLog

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = mapper_registry.metadata


"""
Pure domain bookmark:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""
bio = Table(
    "bio",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user", String(255)),
    Column("weight", Integer),
    Column("bmr", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

dailylog = Table(
    "dailylog",
    metadata,
    Column("ID", Integer, primary_key=True, autoincrement=True),
    Column("IDMeal", Integer),
    Column("MealName", String(255)),
    Column("calories", Integer),
    Column("protein", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

exerciselog = Table(
    "exerciselog",
    metadata,
    Column("ID", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("xfactor", Integer),
    Column("duration", Integer),
    Column("caloriesburned", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

meals = Table(
    "meals",
    metadata,
    Column("ID", Integer, primary_key=True, autoincrement=True),
    Column("name",  String(255)),
    Column("protein", Integer),
    Column("carbs", Integer),
    Column("fats", Integer),
    Column("calories", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

exercise = Table(
    "exercise",
    metadata,
    Column("ID", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("xfactor", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

def start_mappers():
    logger.info("starting mappers")
    fit_mapper = mapper(bio, bio)
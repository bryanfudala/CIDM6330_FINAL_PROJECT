from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from fitlib import bootstrap
from fitlib.domain import commands
from fitlib.services import handlers, unit_of_work
from fitlib.adapters import repository

from fitlib.adapters.orm import start_mappers
from fitlib.services.unit_of_work import AbstractUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=AbstractUnitOfWork())


def test_add_dailylog_item():

    #arrange
    bus = boostrap_test_app()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one = act
    bus.handle(
        commands.AddDailyLogCommand(
            4,
            f"FakeID",  # id meal
            f"broccoli",  # meal name
            250, #calories
            40, #protein
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    print(bus.uow.DailyLogs.get_by_IDMeal(f"FakeID"))

    # assert
    assert bus.uow.DailyLogs.get_by_IDMeal(f"FakeID") is not None
    assert bus.uow.committed



def test_get_all_dailylog_records():
    bus = boostrap_test_app()

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    bus.handle(
        commands.AddDailyLogCommand(
            5,
            f"psuedomealid",  # id meal
            f"chicken",  # meal name
            80, #calories
            10, #protein
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    nuto = nu + timedelta(days=2, hours=12)

    bus.handle(
        commands.AddDailyLogCommand(
            6,
            f"psuedofoodmeal",  # id meal
            f"steak",  # meal name
            100, #calories
            25, #protein
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    records = bus.uow.DailyLogs.get_all()
    assert len(records) == 2
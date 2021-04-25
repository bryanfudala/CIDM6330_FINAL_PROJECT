# START NOTES
"""
Uses guidance from the basic SQLAlchemy 1.4 tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
"""
# END NOTES

from abc import ABC, abstractmethod
from datetime import datetime
from sys import builtin_module_names

# making use of type hints: https://docs.python.org/3/library/typing.html
from typing import List, Set

from fitlib.adapters import orm
from fitlib.domain.models import Bio, DailyLog, ExerciseLog, Meals, Exercise


class AbstractDailyLogRepository(ABC):
    def __init__(self):
        # seen is in reference to events detected
        self.seen : set[DailyLog] = set()

    def add(self, dailylogs: DailyLog) -> None:
        # add to repo
        self._add(DailyLog)
        # add to event list
        self.seen.add(DailyLog)

    def get_all(self) -> list[DailyLog]:
        dailylogs: list[DailyLog] = self._get_all()
        if dailylogs:
            self.seen.update(dailylogs)
        return dailylogs

    def get_by_id(self, value: int) -> DailyLog:
        # get from repo
        DailyLog: DailyLog = self._get_by_id(value)
        if DailyLog:
            self.seen.add(DailyLog)
        return DailyLog        

    @abstractmethod
    def _add(self, DailyLog: DailyLog) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, dailylogs: list[DailyLog]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _get_all(self) -> list[DailyLog]:
        raise NotImplementedError("Derived classes must implement get_all")

    @abstractmethod
    def _get_by_id(self, value: int) -> DailyLog:
        raise NotImplementedError("Derived classes must implement get")


    @abstractmethod
    def _update(self, DailyLog: DailyLog) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, DailyLog: list[DailyLog]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyDailyLogRepository(AbstractDailyLogRepository):


    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, DailyLog: DailyLog) -> None:
        self.session.add(DailyLog)
        self.session.commit()

    def _add_all(self, DailyLogs: list[DailyLog]) -> None:
        self.session.add_all(DailyLogs)
        self.session.commit()

    def _delete(self, DailyLog: DailyLog) -> None:
        pass

    def _get_all(self) -> list[DailyLog]:
        return self.session.query(DailyLog).all()

    def _get_by_id(self, value: int) -> DailyLog:
        answer = self.session.query(DailyLog).filter(DailyLog.id == value)
        return answer.one()

    def _update(self, DailyLog) -> None:
        pass

    def _update(self, DailyLog: list[DailyLog]) -> None:
        pass



class AbstractExerciseLogRepository(ABC):
    def __init__(self):
        self.seen : set[ExerciseLog] = set()

    def add(self, ExerciseLogs: ExerciseLog) -> None:
        self._add(ExerciseLog)
        self.seen.add(ExerciseLog)

    def get_all(self) -> list[ExerciseLog]:
        ExerciseLogs: list[ExerciseLog] = self._get_all()
        if ExerciseLogs:
            self.seen.update(ExerciseLogs)
        return ExerciseLogs

    def get_by_id(self, value: int) -> ExerciseLog:
        # get from repo
        DailyLog: ExerciseLog = self._get_by_id(value)
        if ExerciseLog:
            self.seen.add(ExerciseLog)
        return ExerciseLog        

    @abstractmethod
    def _add(self, ExerciseLog: ExerciseLog) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, ExerciseLogs: list[ExerciseLog]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _get_all(self) -> list[ExerciseLog]:
        raise NotImplementedError("Derived classes must implement get_all")

    @abstractmethod
    def _get_by_id(self, value: int) -> ExerciseLog:
        raise NotImplementedError("Derived classes must implement get")


    @abstractmethod
    def _update(self, ExerciseLog: ExerciseLog) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, ExerciseLog: list[ExerciseLog]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyExerciseLogRepository(AbstractExerciseLogRepository):


    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, ExerciseLog: ExerciseLog) -> None:
        self.session.add(ExerciseLog)
        self.session.commit()

    def _add_all(self, ExerciseLog: list[ExerciseLog]) -> None:
        self.session.add_all(ExerciseLog)
        self.session.commit()

    def _delete(self, ExerciseLog: ExerciseLog) -> None:
        pass

    def _get_all(self) -> list[ExerciseLog]:
        return self.session.query(ExerciseLog).all()

    def _get_by_id(self, value: int) -> ExerciseLog:
        answer = self.session.query(ExerciseLog).filter(ExerciseLog.id == value)
        return answer.one()

    def _update(self, ExerciseLog) -> None:
        pass

    def _update(self, ExerciseLog: list[ExerciseLog]) -> None:
        pass



class AbstractBioRepository(ABC):
    def __init__(self):
        self.seen : set[Bio] = set()

    def add(self, Bios: Bio) -> None:
        self._add(Bio)

        self.seen.add(Bio)

    def get_all(self) -> list[Bio]:
        Bios: list[Bio] = self._get_all()
        if Bio:
            self.seen.update(Bios)
        return Bios

    @abstractmethod
    def _add(self, Bio: Bio) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _update(self, Bio: Bio) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, Bio: list[Bio]) -> None:
        raise NotImplementedError("Derived classes must implement update")

class SqlAlchemyBioRepository(AbstractBioRepository):

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, Bio: Bio) -> None:
        self.session.add(Bio)
        self.session.commit()

    def _get_all(self) -> list[Bio]:
        return self.session.query(Bio).all()

    def _update(self, Bio) -> None:
        pass

    def _update(self, Bio: list[Bio]) -> None:
        pass

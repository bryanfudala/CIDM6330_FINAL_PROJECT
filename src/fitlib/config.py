import os

basedir = os.path.abspath(os.path.dirname(__file__))

def get_sqlite_memory_uri():
    return f"sqlite:///:memory:"


def get_sqlite_file_url():
    """
    gets the fully-qualified path to the bookmarks.db file
    """
    return f"sqlite:///{os.path.join(basedir, 'fitness.db')}"
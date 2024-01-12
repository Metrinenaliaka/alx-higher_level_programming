#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    import sys
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    statement = 'mysql+mysqldb://{}:{}@localhost/{}'.format(arg1, arg2, arg3)
    engine = create_engine(statement, pool_pre_ping=True)
    Base.metadata.create_all(engine)

from sqlalchemy import Column, Text, Integer

from sqlalchemy_bigint_id.testapp.db import Base
from sqlalchemy_bigint_id.types import BigIntegerID


class Coin(Base):
    __tablename__ = 'coin'

    id = Column(BigIntegerID, primary_key=True)
    name = Column(Text)


class Exchange(Base):
    __tablename__ = 'exchange'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

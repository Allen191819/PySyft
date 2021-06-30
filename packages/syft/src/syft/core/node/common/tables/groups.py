# third party
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# relative
from . import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __str__(self):
        return f"<Group id: {self.id}, name: {self.name}>"

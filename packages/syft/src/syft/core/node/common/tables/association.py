# grid relative
# syft relative
from . import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime


class Association(Base):
    """Association.

    Columns:
        id (Integer, Primary Key): Cycle ID.
        date (TIME): Start time.
        network (String): Network name.
        network_address (String) : Network Address.
    """

    __tablename__ = "association"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime())
    name = Column(String(255))
    address = Column(String(255))

    def __str__(self):
        return f"< Association id : {self.id}, Name: {self.name}, Address: {self.address}, Date: {self.date}>"

# grid relative
# syft relative
from . import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey


class UserEnvironment(Base):
    __tablename__ = "userenvironment"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user = Column(Integer, ForeignKey("syft_user.id"))
    environment = Column(Integer, ForeignKey("environment.id"))

    def __str__(self):
        return (
            f"<UserGroup id: {self.id}, user: {self.user}, "
            f"group: {self.environment}>"
        )

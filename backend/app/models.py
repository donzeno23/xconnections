from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

from database import Base
import enum

# metadata_obj = MetaData()

from fastapi_utils.enums import StrEnum

# class UserType(str, enum.Enum):
# NOTE: Enum name and value should match case
# otherwise, get LookupError in sqlalchemy sqltypes
class UserType(StrEnum):
    Client = "Client"
    Vendor = "Vendor"

class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "Users"
    # metadata_obj,
    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # user_id = Column(Integer, primary_key=True, index=True) # auto-generated
    name = Column(String(45))
    email = Column(String(60))
    password = Column(String(20), nullable=True) # blank at signup
    phone = Column(String(20))
    user_type = Column(Enum(UserType)) # vendor or client
    # user_type = Column(String(10))
    sector = Column(String(30)) # empty for Vendor
    pending = Column(String(2)) # Y at signup
    vendors: Mapped["Vendors"] = relationship(back_populates="users") 


class Vendors(Base):
    __tablename__ = "Vendors"
    # metadata_obj,
    # vendor_id = Column(Integer, primary_key=True, index=True)
    vendor_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))
    # user_id = relationship("Users", back_populates="users")
    address1 = Column(String(45))
    address2 = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    country = Column(String(45))
    zipcode = Column(Integer)
    users: Mapped["Users"] = relationship(back_populates="vendors")
    # vendorskills: Mapped["VendorSkills"] = relationship(back_populates="vendor")


class Skills(Base):
    __tablename__ = "Skills"
    # metadata_obj,
    # skill_id = Column(Integer, primary_key=True, index=True)
    skill_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    skill = Column(String(45))


class VendorSkills(Base):
    __tablename__ = "VendorSkills"
    # metadata_obj,
    # id = Column(Integer, primary_key=True, index=True)
    vs_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    vs_vendor_id: Mapped[int] = mapped_column(ForeignKey("Vendors.vendor_id"))
    # vendor = relationship("Vendors", back_populates="vendors")
    # vendor: Mapped["Vendors"] = relationship(back_populates="vendorskills") 
    # skill = relationship("Skills", back_populates="skills")
    vs_skill_id: Mapped[int] = mapped_column(ForeignKey("Skills.skill_id"))
    # vs_skill_id: Mapped["Skills"] = relationship(back_populates="vendorskills") 


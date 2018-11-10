from sqlalchemy import Column, Integer, String
from base import Base


class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column("name", String(100))
    group = Column("group", String(10))
    zach_number = Column(Integer)

    def __init__(self,fname,group, zach_number):
        self.fname =fname
        self.group = group
        self.zach_number = zach_number


    def __repr__(self):
        return "<Student(fname=%s, group=%s, zach_number=%s)" % (self.fname, self.group, self.zach_number)


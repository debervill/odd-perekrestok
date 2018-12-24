from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

path_db = os.path.abspath("db/odd.db")
path = "sqlite:////" + path_db
engine = create_engine(path, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base(engine)
meta = Base.metadata


class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column("name", String(100))
    group = Column("group", String(10))
    zach_number = Column(Integer)

    def __init__(self, fname, group, zach_number):
        self.fname = fname
        self.group = group
        self.zach_number = zach_number

    def __repr__(self):
        return "Student(fname=%s, group=%s, zach_number=%s)" % (self.fname, self.group, self.zach_number)


class KatDorogi(Base):
    __tablename__ = 'KatDor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    kategoria = Column("kategoria", Integer)
    minshirinapolosu = Column("Min Shirina Polosu", Float)
    maxshirinapolosu = Column("Max Shirina Polosu", Float)
    shirinaobochinu = Column("Shirian Obochinu", Float)
    maxpivedinetns = Column("Max Prived Intens", Integer)

    def __init__(self, kategoria, minshirinapolosu, maxshirinapolosu, shirinaobochinu, maxpivedinetns):
        self.kategoria = kategoria
        self.minshirinapolosu = minshirinapolosu
        self.maxshirinapolosu = maxshirinapolosu
        self.shirinaobochinu = shirinaobochinu
        self.maxpivedinetns = maxpivedinetns

    def __repr__(self):
        return "KatDor(kategoria=%s, minshirinapolosu=%s, maxshirinapolosu=%s, shirinaobochinu=%s, maxpivedinetns=%s)" % \
               (self.kategoria, self.minshirinapolosu, self.maxshirinapolosu, self.shirinaobochinu, self.maxpivedinetns)


class Zadanie(Base):
    __tablename__ = 'Zadanie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    N1 = Column("n1", Float)

    def __init__(self,n1):
        self.n1 =  n1

    def __repr__(self):
        return "Zadanie(n1=%s)" %(self.n1)


        
        
        
        
    
   
    
meta.create_all(engine)







from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    education = Column(Text)
    github = Column(String)
    linkedin = Column(String)
    portfolio = Column(String)

    skills = relationship("Skill", back_populates="profile")
    projects = relationship("Project", back_populates="profile")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="skills")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    link = Column(String)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="projects")
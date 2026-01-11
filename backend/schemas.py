from pydantic import BaseModel
from typing import List

class Skill(BaseModel):
    name: str

class Project(BaseModel):
    title: str
    description: str
    link: str

class Profile(BaseModel):
    name: str
    email: str
    education: str
    github: str
    linkedin: str
    portfolio: str
    skills: List[Skill]
    projects: List[Project]

    class Config:
        orm_mode = True
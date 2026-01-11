from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine, Base
from backend.models import Profile, Project, Skill

app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/profile")
def get_profile(db: Session = Depends(get_db)):
    return db.query(Profile).first()


@app.get("/projects")
def get_projects(
    skill: str | None = None,
    db: Session = Depends(get_db)
):
    if skill:
        return (
            db.query(Project)
            .join(Profile)
            .join(Skill)
            .filter(Skill.name.ilike(f"%{skill}%"))
            .all()
        )
    return db.query(Project).all()


@app.get("/skills/top")
def top_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()

@app.get("/search")
def search(
    q: str = Query(...),
    db: Session = Depends(get_db)
):
    return {
        "projects": db.query(Project)
        .filter(Project.title.ilike(f"%{q}%"))
        .all(),
        "skills": db.query(Skill)
        .filter(Skill.name.ilike(f"%{q}%"))
        .all(),
    }
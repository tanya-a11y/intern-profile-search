from backend.database import SessionLocal, engine
from backend.models import Base, Profile, Skill, Project

Base.metadata.create_all(bind=engine)

db = SessionLocal()

profile = Profile(
    name="Tanya Sirohi",
    email="tanya@example.com",
    education="B.Tech in Computer Science",
    github="https://github.com/tanya-ally",
    linkedin="https://www.linkedin.com/in/tanya-sirohi-a6b25b2b9",
    portfolio="https://tanyasirohi.dev"
)

skills = ["Python", "FastAPI", "SQL", "AI", "Machine Learning"]

projects = [
    Project(
        title="AI Circular Economy Marketplace",
        description="Platform connecting sellers with upcycling organizations",
        link="https://github.com/tanyasirohi/ai-circular-economy"
    )
]

db.add(profile)
db.commit()
db.refresh(profile)

for s in skills:
    db.add(Skill(name=s, profile_id=profile.id))

for p in projects:
    p.profile_id = profile.id
    db.add(p)

db.commit()
db.close()

print("Database seeded successfully")
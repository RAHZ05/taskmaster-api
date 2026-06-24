from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from app import models, schemas, database

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="TaskMaster API")

# Dependência para o banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de Criação
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate = Body(...), db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Rota de Leitura
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()
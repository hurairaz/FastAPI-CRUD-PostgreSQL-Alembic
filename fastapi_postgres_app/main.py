from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=404, detail="Email already  exists")
    else:
        return crud.create_user(db, user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_user_item(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db, item, user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(404, "User Not Found")
    return {"message": "User successfully Deleted", "data": db_user}


@app.put("/users/{user_id}")
def update_user(
    user_id: int, updated_user: schemas.UpdateUser, db: Session = Depends(get_db)
):
    db_user = crud.update_user(db, user_id, updated_user)
    if db_user is None:
        raise HTTPException(404, "Could not update")
    return {"message": "User record successfully Updated", "data": db_user}

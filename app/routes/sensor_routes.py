from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth_token import decode_token
from app.core.config import get_db

import app.crud.usuario_crud as crud
import app.schemas.usuario_schemas as schemas


app = APIRouter()


@app.get("/list", dependencies=[Depends(decode_token)])
def list_users(db: Session = Depends(get_db)):
    users = crud.get_usuarios(db=db)
    return users


@app.get("/userId/{usuario_id}", dependencies=[Depends(decode_token)], response_model=schemas.UsuarioBase)
def id_user(usuario_id: int, db: Session = Depends(get_db)):
    user = crud.get_usuario(db=db, usuario_id=usuario_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.UsuarioCreate)
def user_create(
    user: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_usuario(db=db, user=user)


@app.put("/update/{usuario_id}", dependencies=[Depends(decode_token)], response_model=schemas.UsuarioBase)
def user_update( usuario_id: int, user: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    users = crud.actualizar_usuario(
        db=db,
        usuario_id=usuario_id,
        user=user
    )

    if users is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return users


@app.get("/types", dependencies=[Depends(decode_token)])
def list_user_types(db: Session = Depends(get_db)):
    tipos = crud.get_tipos(db)
    return tipos


@app.get("/statuses", dependencies=[Depends(decode_token)])
def list_user_statuses(db: Session = Depends(get_db)):
    estados = crud.get_estados(db)
    return estados
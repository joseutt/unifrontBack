from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.usuario import Usuario

from app.core.security import (
    verify_password,
    create_access_token
)

from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.correo == form_data.username
        )
        .first()
    )

    if not usuario:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo incorrecto"
        )

    if not verify_password(
        form_data.password,
        usuario.password
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password incorrecto"
        )

    access_token = create_access_token(
        data={
            "sub": usuario.correo
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
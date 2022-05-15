from sqlalchemy.orm import Session

from brainstorming.models.sheet import Sheet
import brainstorming.schemas.sheet as sheet_schema


def get_sheets(db: Session):
    return db.query(Sheet).all()


def create_sheet(db: Session, user: user_schema.UserCreateRequest):
    new_user = User(
        login_id=user.login_id,
        name=user.name,
        password_hash=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

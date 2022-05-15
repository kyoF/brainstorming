from sqlalchemy.orm import Session

from brainstorming.models.users import User
import brainstorming.schemas.user as user_schema


def get_user_by_login_id(db: Session, login_id: str):
    return db.query(User).filter_by(login_id=login_id).first()


def create_user(db: Session, user: user_schema.UserCreateRequest):
    new_user = User(
        login_id=user.login_id,
        name=user.name,
        password_hash=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

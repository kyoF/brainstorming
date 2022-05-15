from sqlalchemy.orm import Session

from brainstorming.models.postit import Postit
import brainstorming.schemas as postit_schema


def get_posts(db: Session, sheet_id: int):
    return db.query(Postit).filter(Postit.sheet_id == sheet_id).all()


def create_post(db: Session, postit: postit_schema.PostitCreateRequest):
    new_postit = Postit(
        postit_id=postit.postit_id
        title=postit.title
        remarks=postit.remarks
        xaxis=postit.xaxis
        yaxis=postit.yaxis
        sheet_id=postit.sheet_id
    )
    db.add(new_postit)
    db.commit()
    db.refresh(new_postit)
    return new_postit


def get_post(db: Session, postit_id: int):
    return db.query(Postit).filter_by(id=postit_id).first()

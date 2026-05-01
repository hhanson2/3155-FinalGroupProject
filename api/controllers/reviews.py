from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import reviews as reviews_model


def create(db: Session, review):
    db_review = reviews_model.Review(
        customer_id=review.customer_id,
        order_id=review.order_id,
        review_text=review.review_text,
        score=review.score
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def read_all(db: Session):
    return db.query(reviews_model.Review).all()


def read_one(db: Session, review_id):
    return db.query(reviews_model.Review).filter(reviews_model.Review.id == review_id).first()


def update(db: Session, review_id, review):
    db_review = db.query(reviews_model.Review).filter(reviews_model.Review.id == review_id)
    update_data = review.model_dump(exclude_unset=True)
    db_review.update(update_data, synchronize_session=False)
    db.commit()
    return db_review.first()


def delete(db: Session, review_id):
    db_review = db.query(reviews_model.Review).filter(reviews_model.Review.id == review_id)
    db_review.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
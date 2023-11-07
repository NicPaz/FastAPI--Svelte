from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    # SELECT * from users where id = user_id
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    # SELECT * from users where id = user_id
    return db.query(models.User).filter(models.User.id == user_id).delete()

def create_favorite_movie(db: Session, favorite_movie: schemas.FavoriteMovieCreate, user_id: int):
    db_favorite_movie = models.FavoriteMovie(movie_id=favorite_movie.movie_id, user_id=user_id)
    db.add(db_favorite_movie)
    db.commit()
    db.refresh(db_favorite_movie)
    return db_favorite_movie

def get_favorite_movies(db: Session, user_id: int):
    return db.query(models.FavoriteMovie).filter(models.FavoriteMovie.user_id == user_id).all()


def delete_favorite_movie(db: Session, favorite_movie_id: int):
    favorite_movie = db.query(models.FavoriteMovie).filter(models.FavoriteMovie.id == favorite_movie_id).first()
    if favorite_movie:
        db.delete(favorite_movie)
        db.commit()
        return favorite_movie
    return None

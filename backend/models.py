from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class FavoriteMovie(Base):
    __tablename__ = "favorite_movies"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

class FavoriteArtist(Base):
    __tablename__ = "favorite_artist"
    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

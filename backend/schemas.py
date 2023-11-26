from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool    
    class Config:
        orm_mode = True

class FavoriteMovieBase(BaseModel):
    movie_id: int

class FavoriteMovieCreate(FavoriteMovieBase):
    pass

class FavoriteMovie(FavoriteMovieBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class FavoriteArtistBase(BaseModel):
    artist_id: int

class FavoriteArtistCreate(FavoriteArtistBase):
    pass

class FavoriteArtist(FavoriteArtistBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
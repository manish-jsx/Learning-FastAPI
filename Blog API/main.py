# main.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Model for User
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Model for Blog
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="blogs")
    comments = relationship("Comment", back_populates="blog")

# Model for Comment
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    
    blog = relationship("Blog", back_populates="comments")

Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

# Dependency to get the current user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, db)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password hashing
password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token verification
def verify_token(token: str, db: Session):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

# CRUD operations for users
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = password_hash.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD operations for blogs
def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Blog).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: schemas.BlogCreate, current_user: User):
    db_blog = Blog(**blog.dict(), owner_id=current_user.id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

# CRUD operations for comments
def create_comment(db: Session, comment: schemas.CommentCreate, blog_id: int, current_user: User):
    db_comment = Comment(**comment.dict(), blog_id=blog_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# API endpoints

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return create_access_token(
        data={"sub": form_data.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/blogs/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = get_blogs(db, skip=skip, limit=limit)
    return blogs

@app.post("/blogs/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_blog(db=db, blog=blog, current_user=current_user)

@app.post("/blogs/{blog_id}/comments/", response_model=schemas.Comment)
def create_comment_for_blog(blog_id: int, comment: schemas.CommentCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_comment(db=db, comment=comment, blog_id=blog_id, current_user=current_user)



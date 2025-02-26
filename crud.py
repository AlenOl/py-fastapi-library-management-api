from sqlalchemy.orm import Session
import models
import schemas


def get_all_authors(db: Session) -> list[models.Author]:
    return db.query(models.Author).all()


def get_authors_by_name(db: Session, name: str) -> models.Author:
    return (
        db.query(models.Author).filter(models.Author.name == name).first()
    )


def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    db_author = models.Author(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int) -> models.Author:
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_all_books(db: Session) -> list[models.Book]:
    return db.query(models.Book).all()


def get_books_list(
    db: Session,
    title: str | None = None,
    author_id: int | None = None,
) -> list[models.Book]:
    queryset = db.query(models.Book)
    if title is not None:
        queryset = queryset.filter(
            models.Book.title == title
        )

    if author_id is not None:
        queryset = queryset.filter(models.Book.author_id == author_id)

    return queryset.all()


def get_book(db: Session, author_id: int) -> models.Book:
    return db.query(models.Book).filter(models.Book.author_id == author_id).first()


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

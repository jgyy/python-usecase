"""
create table products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER NOT NULL,
    published BOOLEAN NOT NULL DEFAULT false,
    created_on TIMESTAMP NOT NULL DEFAULT NOW()
);
alter table products ADD CONSTRAINT level_check CHECK (
    level >= 0
    AND level <= 2
);
create table reviews (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    rating INTEGER NOT NULL,
    comment TEXT,
    created_on TIMESTAMP NOT NULL DEFAULT NOW()
);
alter table reviews add constraint rating_check CHECK (
    rating > 0
    AND rating <= 5
);
"""
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from dbexport.config import session_class

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    published = Column(Boolean)
    created_on = Column(TIMESTAMP)

    reviews = relationship("Review", order_by="Review.rating", back_populates="product")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_on = Column(TIMESTAMP)

    product = relationship("Product", back_populates="reviews")


if __name__ == "__main__":
    os.environ["DB_URL"] = "postgres://jgyy:jgyy@13.229.62.87:80/reviews"
    Session = session_class()
    session = Session()
    print(session.query(func.count(Product.id)))
    print(session.query(func.count(Product.id)).all())
    products = session.query(Product).limit(5).all()
    print(products)
    for product in products:
        print(product.name)
    print(products[0].reviews)

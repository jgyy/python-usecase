"""
name,level,published,created_on,review_count,avg_rating
Product 1,1,True,2019-07-10,10,4.3
"""
import os
import csv
from dbexport.config import session_class
from dbexport.models import Product, Review
from sqlalchemy.sql import func

os.environ["DB_URL"] = "postgres://jgyy:jgyy@13.229.62.87:80/reviews"
Session = session_class()

csv_file = open("product_ratings.csv", mode="w")
fields = ["name", "level", "published", "created_on", "review_count", "avg_rating"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
csv_writer.writeheader()

session = Session()

reviews_statement = (
    session.query(
        Review.product_id,
        func.count("*").label("review_count"),
        func.avg(Review.rating).label("avg_rating"),
    )
    .group_by(Review.product_id)
    .subquery()
)

for product, review_count, avg_rating in session.query(
    Product, reviews_statement.c.review_count, reviews_statement.c.avg_rating
).outerjoin(reviews_statement, Product.id == reviews_statement.c.product_id):
    csv_writer.writerow(
        {
            "name": product.name,
            "level": product.level,
            "published": product.published,
            "created_on": product.created_on.date(),
            "review_count": review_count or 0,
            "avg_rating": round(float(avg_rating), 4) if avg_rating else 0,
        }
    )

csv_file.close()

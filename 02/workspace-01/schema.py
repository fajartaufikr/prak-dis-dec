import strawberry
from typing import List
from strawberry.asgi import GraphQL

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        return [
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
            Book(title="Harry Potter", author="J.K. Rowling"),
        ]

schema = strawberry.Schema(query=Query)

app = GraphQL(schema)
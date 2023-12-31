from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType

class Timestamp(BaseModel):
    id: int
    timestamp: int

dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]
@app.get("/")
def root():
    return {'Hello, World!'}

@app.post("/post")
def get_post():
    return post_db[0]

@app.get("/dog")
def get_dogs(kind: DogType):
    dogs = [dog for dog in dogs_db.values() if dog.kind == kind]
    return dogs

@app.post("/dog")
def create_dog(dog: Dog):
    dogs_db[max(dogs_db.keys())+1] = dog
    return dog

@app.get("/dog/{pk}")
def get_dog_by_pk(pk : int):
    dogs = [dog for dog in dogs_db.values() if dog.pk == pk]
    return dogs 

@app.patch("/dog/{pk}")
def update_dog(pk : int, dog_body : Dog):
    for i in dogs_db:
        if dogs_db[i].pk == pk:
            dogs_db[i] = dog_body
    return dog_body
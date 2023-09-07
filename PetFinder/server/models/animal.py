from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, validator


class Breeds(BaseModel):
    primary: str
    secondary: Optional[str]
    mixed: bool
    unknown: bool


class Colors(BaseModel):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]


class Attributes(BaseModel):
    spayed_neutered: bool
    house_trained: bool
    declawed: Optional[bool]
    special_needs: bool
    shots_current: bool


class Environment(BaseModel):
    children: Optional[bool]
    dogs: Optional[bool]
    cats: Optional[bool]


class Photo(BaseModel):
    small: str
    medium: str
    large: str
    full: str


class Video(BaseModel):
    embed: str


class Address(BaseModel):
    address1: Optional[str]
    address2: Optional[str]
    city: str
    state: str
    postcode: str
    country: str


class Contact(BaseModel):
    email: Optional[str]
    phone: Optional[str]
    address: Address


class Self(BaseModel):
    href: str


class Type(BaseModel):
    href: str


class Organization(BaseModel):
    href: str


class Links(BaseModel):
    self: Self
    type: Type
    organization: Organization

class Animal(BaseModel):
    id: int
    organization_id: str
    url: str
    type: str
    species: str
    breeds: Breeds
    colors: Colors
    age: str
    gender: str
    size: str
    coat: Any
    attributes: Attributes
    environment: Environment
    tags: List[str]
    name: str
    description: str
    @validator('description')
    def default_description(cls, val: str) -> str:
        if not val or val.strip() == '':
            return 'no description'
        return val.replace("&amp;#39;", "'")

    photos: List[Photo]
    @validator('photos')
    def always_exist(cls, val:List[Photo]) -> List[Photo]:
        if(len(val)==0):
            return [Photo(small='http://127.0.0.1:8000/no_image', medium='http://127.0.0.1:8000/no_image', large='http://127.0.0.1:8000/no_image', full='http://127.0.0.1:8000/no_image')]
        return val
    videos: List[Video]
    status: str
    published_at: str
    contact: Contact
    _links: Links
from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel, Field


class Branche(BaseModel):
    branche_id: str = Field(..., alias='brancheId')
    mandatory: Optional[bool] = Field(..., alias='verplicht')
    maximum: Optional[int] = Field(..., alias='maximumPlaatsen')


class Obstacle(BaseModel):
    from_location: str = Field(..., alias="kraamA")
    to_location: str = Field(..., alias="kraamB")
    obstacle: List[str] = Field(..., alias='obstakel')


class Geography(BaseModel):
    obstacles: List[Obstacle] = Field(..., alias='obstakels')


class Location(BaseModel):
    place_id: str = Field(..., alias='plaatsId')
    branches: Optional[List[str]]
    options: Optional[List[str]] = Field(..., alias='verkoopinrichting')
    properties: Optional[List[str]]


class Rows(BaseModel):
    rows: List[List[str]]


class ListGroup(BaseModel):
    style_class: str = Field(..., alias='class')
    title: str
    landmark_top: str = Field(..., alias='landmarkTop')
    landmark_bottom: str = Field(..., alias='landmarkBottom')
    place_list: List[str] = Field(..., alias='plaatsList')


class Page(BaseModel):
    title: str
    list_group: List[ListGroup] = Field(..., alias='indelingslijstGroup')

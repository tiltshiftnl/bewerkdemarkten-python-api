from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel, Field


class Branche(BaseModel):
    branche_id: str = Field(...,alias='brancheId')
    number: Optional[int] = None
    description: Optional[str] = None
    color: Optional[str] = None


class Plan(BaseModel):
    name: str
    pages: Optional[int]


class Announcement(BaseModel):
    activation: str = Field(...,alias='activatie')
    staging_period: str = Field(...,alias='wenperiode')
    live: str = Field(...,alias='live')


class Announcements(BaseModel):
    market_detail: Announcement = Field(...,alias='marktDetail')
    market_detail_properties: Announcement = Field(...,alias='marktDetailPlaatsvoorkeuren')
    presence: Announcement = Field(...,alias='aanwezigheid')
    properties: Announcement = Field(...,alias='plaatsVoorkeuren')


class Event(BaseModel):
    weekday: Optional[int] = None
    plan: Optional[Plan] = None


class Market(BaseModel):
    market_id: Optional[int] = Field(...,alias='id')
    name: Optional[str] = None
    phase: Optional[str] = None
    plan: Optional[Plan] = None
    events: Dict[str, Event]


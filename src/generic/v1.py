from fastapi import APIRouter, Depends, Request
from typing import List, Dict, Optional
from ..models.generic import Branche, Announcements, Market
from ..dependencies import get_user
import json
router = APIRouter()

basedir = '/tmp/bewerkdemarkten-repo/config/markt/'


@router.get("/api/v1/markt/mededelingen.json", response_model=Announcements, response_model_exclude_none=True, response_model_by_alias=True)
def get_announcements(user: str = Depends(get_user)):
    with open(basedir + 'mededelingen.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.get("/api/v1/markt/branches.json", response_model=List[Branche], response_model_exclude_none=True, response_model_by_alias=True)
def get_branches(user: str = Depends(get_user)):
    with open(basedir + 'branches.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/branches.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_branches(user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/daysClosed.json", response_model=List[str])
def get_days_closed(user: str = Depends(get_user)):
    with open(basedir + 'daysClosed.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.get("/api/v1/markets.json", response_model=Optional[Dict[str, Market]], response_model_exclude_none=True, response_model_by_alias=True)
def get_markets(user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/obstakeltypes.json", response_model=List[str])
def get_obstacle_types(user: str = Depends(get_user)):
    with open(basedir + 'obstakeltypes.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.get("/api/v1/markt/plaatseigenschappen.json", response_model=List[str], response_model_exclude_none=True, response_model_by_alias=False)
def get_properties(user: str = Depends(get_user)):
    with open(basedir + 'plaatseigenschappen.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj

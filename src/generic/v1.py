import os
from fastapi import APIRouter, Depends, Request
from typing import List, Dict, Optional
from ..models.generic import Branche, Announcements, Market, MarketEvent, Plan
from ..dependencies import get_user
import json
from pathlib import Path
router = APIRouter()

basedir = '/tmp/bewerkdemarkten-repo/config/markt/'
pdfdir = '/tmp/bewerkdemarkten-repo/dist/pdf/'

week_days = {
    "MA": 1,
    "DI": 2,
    "WO": 3,
    "DO": 4,
    "VR": 5,
    "ZA": 6,
    "ZO": 7
}


def get_event(market: str, day: str) -> MarketEvent:
    result = MarketEvent(
        weekday=week_days.get(day, None)
    )
    if os.path.isfile(pdfdir + "kaart-" + market + '-' + day + ".pdf"):
        result.plan = Plan(
            name="kaart-" + market + '-' + day
        )

    return result


def set_market():
    return "Not implemented"


def find_pdf_file(filename: str):
    return "Not implemented"


def read_markets() -> Dict[str, Market]:
    markets: Markets={}
    i=0
    for dirpath, dirs, file in os.walk(basedir):
        i=i + 1
        folder_name=(os.path.basename(dirpath))
        print(folder_name)
        market=folder_name.split("-")
        if market[0] != '':
            if market[0] in markets:
                markets[market[0]].events[market[1]
                    ] = get_event(market[0], market[1])
            else:
                events= {}
                events[market[1]]= get_event(market[0], market[1])
                new_market = Market(
                    id = i,
                    events = events
                )
                
                if os.path.isfile(pdfdir + "kaart-" + market[0] + ".pdf"):
                    print("Yes, we got a plan!")
                    new_market.plan = Plan(
                        name="kaart-" + market[0]
                    )

                markets[market[0]] = new_market

    # print(markets)
    return markets


def read_file(filename: str):
    return "Not implemented"

##
# Routes
##


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
    return read_markets()



@router.get("/api/v1/markt/obstakeltypes.json", response_model=List[str])
def get_obstacle_types(user: str = Depends(get_user)):
    with open(basedir + 'obstakeltypes.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.get("/api/v1/markt/plaatseigenschappen.json", response_model=List[str])
def get_properties(user: str = Depends(get_user)):
    with open(basedir + 'plaatseigenschappen.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj

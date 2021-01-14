from fastapi import APIRouter, Depends, Request, HTTPException
from typing import List
from ..dependencies import get_user
from ..models.market import Branche, Geography, Location, Rows, Page
import json
router = APIRouter()


basedir = '/tmp/bewerkdemarkten-repo/config/markt/'


def read_file(filename: str):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/branches.json", response_model=List[Branche], response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_branches(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'branches.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/branches.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_branches(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/geografie.json", response_model=Geography, response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'geografie.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/geografie.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/locaties.json", response_model=List[Location], response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_locations(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'locaties.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/locaties.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_locations(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/markt.json", response_model=Rows, response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_rows(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'markt.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/markt.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_rows(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/paginas.json", response_model=List[Page], response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_pages(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'paginas.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/paginas.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_pages(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/download/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/upload/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.delete("/api/v1/markt/{market_day}/delete/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def delete_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"

from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy import exc
from sqlalchemy.orm import Session
from ..dependencies import get_user

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/markt/{market_day}/branches.json", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_branches(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/branches.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_branches(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/geografie.json", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_geografie(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/geografie.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_geografie(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/locaties.json", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_locations(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/locaties.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_locations(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/markt.json", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_rows(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/markt.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_rows(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/paginas.json", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_pages(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/paginas.json", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_pages(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/download/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def get_market_day_pdf(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.post("/api/v1/markt/{market_day}/upload/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def post_market_day_pdf(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"


@router.delete("/api/v1/markt/{market_day}/delete/pdf", response_model_exclude_none=True, response_model_by_alias=False)
def delete_market_day_pdf(db: Session = Depends(get_db), user: str = Depends(get_user)):
    return "Not implemented"

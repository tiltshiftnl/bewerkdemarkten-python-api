import os
import re
from pathlib import Path
from fastapi import APIRouter, Depends, Request, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
from ..dependencies import get_user
from ..models.market import Branche, Geography, Location, Rows, Page
import json
from ..settings import settings
router = APIRouter()

basedir = settings.JSON_DIR
pdfdir = settings.PDF_DIR


def check_market_day(market_day: str) -> bool:
    pattern = "^[A-Za-z0-9_-]*$"
    if bool(re.match(pattern, market_day)) == True:
        return True
    else:
        raise HTTPException(status_code=400, detail="Invalid Market Day")


@router.get("/api/v1/markt/{market_day}/branches.json", response_model=List[Branche], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_branches(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        try:
            with open(basedir + market_day + "/" + 'branches.json', 'r') as myfile:
                data = myfile.read()

            obj = json.loads(data)
            return obj
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"branches.json for {market_day} could not be found")


@router.post("/api/v1/markt/{market_day}/branches.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_branches(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/api/v1/markt/{market_day}/geografie.json", response_model=Geography, response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        try:
            with open(basedir + market_day + "/" + 'geografie.json', 'r') as myfile:
                data = myfile.read()

            obj = json.loads(data)
            return obj
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"geografie.json for {market_day} could not be found")
    

@router.post("/api/v1/markt/{market_day}/geografie.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/api/v1/markt/{market_day}/locaties.json", response_model=List[Location], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_locations(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        try:
            with open(basedir + market_day + "/" + 'locaties.json', 'r') as myfile:
                data = myfile.read()

            obj = json.loads(data)
            return obj
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"geografie.json for {market_day} could not be found")

@router.post("/api/v1/markt/{market_day}/locaties.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_locations(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/api/v1/markt/{market_day}/markt.json", response_model=Rows, response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_rows(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        with open(basedir + market_day + "/" + 'markt.json', 'r') as myfile:
            data = myfile.read()

        obj = json.loads(data)
        return obj


@router.post("/api/v1/markt/{market_day}/markt.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_rows(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        raise HTTPException(status_code=501, detail="Not implemented")

    


@router.get("/api/v1/markt/{market_day}/paginas.json", response_model=List[Page], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_pages(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        try:
            with open(basedir + market_day + "/" + 'paginas.json', 'r') as myfile:
                data = myfile.read()

            obj = json.loads(data)
            return obj
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"geografie.json for {market_day} could not be found")

@router.post("/api/v1/markt/{market_day}/paginas.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_pages(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/api/v1/markt/{market_day}/download/pdf")
def get_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        if os.path.isfile(pdfdir + "kaart-" + market_day + ".pdf"):
            return FileResponse(pdfdir + "kaart-" + market_day + ".pdf")

        raise HTTPException(status_code=404, detail="plan not found, nothing to download")


# Be aware! Requires python-multipart to be installed
@router.post("/api/v1/markt/{market_day}/upload/pdf")
async def post_market_day_pdf(market_day: str, file: UploadFile = File(...), user: str = Depends(get_user)):
    if check_market_day(market_day):
        file_location = f"{pdfdir}kaart-{market_day}.pdf"
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())

        return {'filename': file.filename}


@router.delete("/api/v1/markt/{market_day}/delete/pdf")
def delete_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    if check_market_day(market_day):
        if os.path.isfile(pdfdir + "kaart-" + market_day + ".pdf"):
            os.remove(pdfdir + "kaart-" + market_day + ".pdf")
            return "ok"

        raise HTTPException(status_code=404, detail="plan not found, nothing to delete")

import os
from fastapi import APIRouter, Depends, Request, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
from ..dependencies import get_user
from ..models.market import Branche, Geography, Location, Rows, Page
import json
router = APIRouter()


basedir = '/tmp/bewerkdemarkten-repo/config/markt/'
pdfdir = '/tmp/bewerkdemarkten-repo/dist/pdf/'

def read_file(filename: str):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/branches.json", response_model=List[Branche], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_branches(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'branches.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/branches.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_branches(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/geografie.json", response_model=Geography, response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'geografie.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/geografie.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_geografie(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/locaties.json", response_model=List[Location], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_locations(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'locaties.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/locaties.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_locations(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/markt.json", response_model=Rows, response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_rows(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'markt.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/markt.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_rows(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/paginas.json", response_model=List[Page], response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_pages(market_day: str, user: str = Depends(get_user)):
    with open(basedir + market_day + "/" + 'paginas.json', 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    return obj


@router.post("/api/v1/markt/{market_day}/paginas.json", response_model_exclude_none=True, response_model_by_alias=True)
def post_market_day_pages(market_day: str, user: str = Depends(get_user)):
    return "Not implemented"


@router.get("/api/v1/markt/{market_day}/download/pdf", response_model_exclude_none=True, response_model_by_alias=True)
def get_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    if os.path.isfile(pdfdir + "kaart-" + market_day + ".pdf"):
        return FileResponse(pdfdir + "kaart-" + market_day + ".pdf")

# Be aware! Requires python-multipart to be installed
@router.post("/api/v1/markt/{market_day}/upload/pdf")
async def post_market_day_pdf(market_day: str, file: UploadFile = File(...), user: str = Depends(get_user)):
    file_location = f"{pdfdir}kaart-{market_day}.pdf"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    return {'filename': file.filename}


@router.delete("/api/v1/markt/{market_day}/delete/pdf", response_model_exclude_none=True, response_model_by_alias=True)
def delete_market_day_pdf(market_day: str, user: str = Depends(get_user)):
    if os.path.isfile(pdfdir + "kaart-" + market_day + ".pdf"):
        os.remove(pdfdir + "kaart-" + market_day + ".pdf")
        return "ok"

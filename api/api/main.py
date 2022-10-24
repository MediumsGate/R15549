from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.services.geo_vector_service import GeoVectorService, GeoJsonService

api = FastAPI()

origins = [
    "http://localhost:5173",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


service: GeoVectorService = GeoJsonService()


@api.get('/get_geo_vector_data')
def get_geo_vector_data(area_of_interest: str, year: int, quarter: str, version: int):

    try:
        json_data = service.get_geo_vector_data(
            area_of_interest=area_of_interest.capitalize(),
            year=year,
            quarter=quarter,
            version=version
        )
    except ValueError:
        interest = {"area_of_interest": area_of_interest, "year": year, "quarter": quarter, "version": version}
        raise HTTPException(status_code=404, detail=f"No area of interest found for: {interest}")

    return json_data

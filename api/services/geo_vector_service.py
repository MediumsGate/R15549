from typing import Protocol, Union
import os
import json


LOCAL_DIR: str = os.path.dirname(__file__)


class GeoVectorService(Protocol):

    @staticmethod
    def get_geo_vector_data(area_of_interest: str, year: int, quarter: str, version: int) -> Union[dict, None]:
        ...


class GeoJsonService:

    @staticmethod
    def get_geo_vector_data(area_of_interest: str, year: int, quarter: str, version: int) -> Union[dict, None]:

        data_path: str = os.path.join(LOCAL_DIR, f'areas_of_interest/{area_of_interest.capitalize()}_{year}'
                                                 f'Q{quarter}_V{version}_AOI.geojson')

        try:
            json_data = json.load(open(data_path))
        except FileNotFoundError:
            raise ValueError

        return json_data


def main():

    service: GeoVectorService = GeoJsonService()
    interest: dict = {
        "area_of_interest": "wellington",
        "year": 21,
        "quarter": 3,
        "version": 0,
    }

    try:
        print(service.get_geo_vector_data(**interest))
    except ValueError:
        print(f"No area of interest found for: {interest}")


if __name__ == "__main__":
    main()
